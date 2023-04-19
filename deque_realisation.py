# ID_1 = 85860585
# ID_2 = 85953970
# ID_3 = 86028900

import logging


from exceptions import OperationError


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)


class Deque:

    def __init__(self, max_size: int) -> None:
        self.__max_size: int = max_size
        self.__head: int = self.__max_size - 1
        self.__tail: int = 0
        self.__items: list = [None] * max_size
        self.__size: int = 0

    def __logging(self) -> None:
        """Осуществляет логирование"""
        logging.debug(self.__items)
        logging.debug(self.__head)
        logging.debug(self.__tail)
        logging.debug(self.__size)

    @property
    def __is_full(self) -> bool:
        return self.__size == self.__max_size

    @property
    def __is_empty(self) -> bool:
        return self.__size == 0

    def push_back(self, value: int):
        """
        добавить элемент в конец дека.
        Если в деке уже находится максимальное число элементов,
        вывести «error».
        """
        if self.__is_full:
            raise OperationError('error')
        self.__items[self.__tail] = value
        self.__tail += 1
        self.__size += 1
        if self.__tail == self.__max_size:
            self.__tail = 0
        self.__logging()

    def push_front(self, value: int):
        """
        добавить элемент в начало дека.
        Если в деке уже находится максимальное число элементов,
        вывести «error».
        """
        if self.__is_full:
            raise OperationError('error')
        if self.__head == 0 and self.__size != 0:
            self.__items[self.__head] = value
            self.__head = self.__max_size - 1
            self.__size += 1
            self.__logging()
        else:
            self.__size += 1
            self.__items[self.__head] = value
            self.__head -= 1
            self.__logging()

    def pop_front(self):
        """
        вывести первый элемент дека и удалить его.
        Если дек был пуст, то вывести «error».
        """
        if self.__is_empty:
            raise OperationError('error')
        self.__size -= 1
        if self.__head == self.__max_size - 1:
            result = self.__items[0]
            self.__items[0] = None
            self.__head = 0
            self.__logging()
            return result
        result = self.__items[self.__head + 1]
        self.__items[self.__head + 1] = None
        self.__head += 1
        if self.__size == 0:
            self.__tail = 0
            self.__head = self.__max_size - 1
        self.__logging()
        return result

    def pop_back(self):
        """
        вывести последний элемент дека и удалить его.
        Если дек был пуст, то вывести «error».
        """
        if self.__is_empty:
            raise OperationError('error')
        self.__size -= 1
        if self.__tail == 0:
            result = self.__items[self.__max_size - 1]
            self.__items[self.__max_size - 1] = None
            self.__tail = self.__max_size - 1
            if self.__size == 0:
                self.__tail = 0
                self.__head = self.__max_size - 1
            self.__logging()
            return result
        else:
            result = self.__items[self.__tail-1]
            self.__items[self.__tail-1] = None
            self.__tail -= 1
            if self.__size == 0:
                self.__tail = 0
                self.__head = self.__max_size - 1
            self.__logging()
            return result


if __name__ == '__main__':
    number_commands = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for command in range(number_commands):
        command = input().split()
        try:
            if len(command) > 1:
                method_name = command[0]
                method_to_call = getattr(deque, method_name)
                method_to_call(command[1])
            else:
                method_name = command[0]
                method_to_call = getattr(deque, method_name)
                print(method_to_call())
        except OperationError as error_message:
            print(error_message)
