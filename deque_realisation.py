# ID = 85860585

import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO)


class Deque:

    def __init__(self, max_size: int) -> None:
        self.max_size: int = max_size
        self.head: int = 0
        self.tail: int = 0
        self.items: list = [None] * max_size
        self.size: int = 0

    def __is_full(self) -> bool:
        return self.size == self.max_size

    def __is_empty(self):
        return self.size == 0

    def push_back(self, value: int):
        """
        добавить элемент в конец дека.
        Если в деке уже находится максимальное число элементов,
        вывести «error».
        """
        if not self.__is_full() and self.size == 0:
            self.tail = 0
            self.items[self.tail] = value
            self.head = self.max_size - 1
            self.tail += 1
            self.size += 1
            logging.debug(self.items)
            logging.debug(self.head)
            logging.debug(self.tail)
            logging.debug(self.size)
            return
        if not self.__is_full():
            self.items[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
            logging.debug(self.items)
            logging.debug(self.head)
            logging.debug(self.tail)
            logging.debug(self.size)
            return
        return 'error'

    def push_front(self, value: int):
        """
        добавить элемент в начало дека.
        Если в деке уже находится максимальное число элементов,
        вывести «error».
        """
        if self.__is_full():
            return 'error'
        if self.head == 0 and self.size == 0:
            self.items[self.head] = value
            self.head = self.max_size - 1
            self.tail += 1
            self.size += 1
            logging.debug(self.items)
            logging.debug(self.head)
            logging.debug(self.tail)
            logging.debug(self.size)
        elif self.head == 0 and self.size != 0:
            self.items[self.head] = value
            self.head = self.max_size - 1
            self.size += 1
            logging.debug(self.items)
            logging.debug(self.head)
            logging.debug(self.tail)
            logging.debug(self.size)
        else:
            self.size += 1
            self.items[self.head] = value
            self.head -= 1
            logging.debug(self.items)
            logging.debug(self.head)
            logging.debug(self.tail)
            logging.debug(self.size)

    def pop_front(self):
        """
        вывести первый элемент дека и удалить его.
        Если дек был пуст, то вывести «error».
        """
        if self.__is_empty():
            return 'error'
        self.size -= 1
        if self.head == self.max_size - 1 and self.size == 0:
            result = self.items[0]
            self.items[0] = None
            self.head = 0
            self.tail = 0
            logging.debug(self.items)
            logging.debug(self.head)
            logging.debug(self.tail)
            logging.debug(self.size)
            return result
        if self.head == self.max_size - 1:
            result = self.items[0]
            self.items[0] = None
            self.head = 0
            logging.debug(self.items)
            logging.debug(self.head)
            logging.debug(self.tail)
            logging.debug(self.size)
            return result
        result = self.items[self.head + 1]
        self.items[self.head + 1] = None
        self.head += 1
        if self.size == 0:
            self.tail = 0
            self.head = 0
        logging.debug(self.items)
        logging.debug(self.head)
        logging.debug(self.tail)
        logging.debug(self.size)
        return result

    def pop_back(self):
        """
        вывести последний элемент дека и удалить его.
        Если дек был пуст, то вывести «error».
        """
        if self.__is_empty():
            return 'error'
        self.size -= 1
        if self.tail == 0:
            result = self.items[self.max_size - 1]
            self.items[self.max_size - 1] = None
            self.tail = self.max_size - 1
            if self.size == 0:
                self.tail = 0
                self.head = 0
            logging.debug(self.items)
            logging.debug(self.head)
            logging.debug(self.tail)
            logging.debug(self.size)
            return result
        else:
            result = self.items[self.tail-1]
            self.items[self.tail-1] = None
            self.tail -= 1
            if self.size == 0:
                self.tail = 0
                self.head = 0
            logging.debug(self.items)
            logging.debug(self.head)
            logging.debug(self.tail)
            logging.debug(self.size)
            return result


if __name__ == '__main__':
    number_commands = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for command in range(number_commands):
        command = input()
        if 'push_front' in command:
            result = deque.push_front(int(command.split()[1]))
            if result == 'error':
                print('error')
        elif 'push_back' in command:
            result = deque.push_back(int(command.split()[1]))
            if result == 'error':
                print('error')
        elif command == 'pop_front':
            print(deque.pop_front())
        elif command == 'pop_back':
            print(deque.pop_back())
        else:
            raise ValueError('неожидаемое значение')
