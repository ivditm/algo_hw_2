# ID_1 = 85860585
# ID_2 = 85953970

import logging


from exceptions import OperationError


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)


class Deque:

    def __init__(self, max_size: int) -> None:
        self.max_size: int = max_size
        # я овощь - не понял, почему неправильно?
        # 1 сдвигаем влево -> 0
        self.head: int = 0
        self.tail: int = 0
        self.items: list = [None] * max_size
        self.size: int = 0

    @property
    def __logging(self) -> None:
        """Осуществляет логирование"""
        logging.debug(self.items)
        logging.debug(self.head)
        logging.debug(self.tail)
        logging.debug(self.size)

    def __is_full(self) -> bool:
        return self.size == self.max_size

    def __is_empty(self) -> bool:
        return self.size == 0

    def push_back(self, value: int):
        """
        добавить элемент в конец дека.
        Если в деке уже находится максимальное число элементов,
        вывести «error».
        """
        # теперь сначала значение - потом указатель
        # честно, вообще не понимаю фишку с (...)%self.max_size
        if self.__is_full():
            raise OperationError('error')
        if self.tail == 0 and self.size == 0:
            self.items[self.tail] = value
            self.head = self.max_size - 1
            self.tail += 1
            self.size += 1
            self.__logging
        else:
            self.items[self.tail] = value
            self.tail += 1
            self.size += 1
            if self.tail == self.max_size:
                self.tail = 0
            self.__logging

    def push_front(self, value: int):
        """
        добавить элемент в начало дека.
        Если в деке уже находится максимальное число элементов,
        вывести «error».
        """
        if self.__is_full():
            raise OperationError('error')
        if self.head == 0 and self.size == 0:
            self.items[self.head] = value
            self.head = self.max_size - 1
            self.tail += 1
            self.size += 1
            self.__logging
        elif self.head == 0 and self.size != 0:
            self.items[self.head] = value
            self.head = self.max_size - 1
            self.size += 1
            self.__logging
        else:
            self.size += 1
            self.items[self.head] = value
            self.head -= 1
            self.__logging

    def pop_front(self):
        """
        вывести первый элемент дека и удалить его.
        Если дек был пуст, то вывести «error».
        """
        if self.__is_empty():
            raise OperationError('error')
        self.size -= 1
        if self.head == self.max_size - 1 and self.size == 0:
            result = self.items[0]
            self.items[0] = None
            self.head = self.tail = 0
            self.__logging
            return result
        if self.head == self.max_size - 1:
            result = self.items[0]
            self.items[0] = None
            self.head = 0
            self.__logging
            return result
        result = self.items[self.head + 1]
        self.items[self.head + 1] = None
        self.head += 1
        if self.size == 0:
            self.tail = self.head = 0
        self.__logging
        return result

    def pop_back(self):
        """
        вывести последний элемент дека и удалить его.
        Если дек был пуст, то вывести «error».
        """
        if self.__is_empty():
            raise OperationError('error')
        self.size -= 1
        if self.tail == 0:
            result = self.items[self.max_size - 1]
            self.items[self.max_size - 1] = None
            self.tail = self.max_size - 1
            if self.size == 0:
                self.tail = self.head = 0
            self.__logging
            return result
        else:
            result = self.items[self.tail-1]
            self.items[self.tail-1] = None
            self.tail -= 1
            if self.size == 0:
                self.tail = self.head = 0
            self.__logging
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
