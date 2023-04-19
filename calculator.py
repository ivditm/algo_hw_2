# ID_1 = 85882520
# ID_2 = 85941877
# ID_3 = 85988605

from exceptions import OperationError

OPERATORS = {'+': '__add__',
             '-': '__sub__',
             '*': '__mul__',
             '/': '__floordiv__'}


class Stack:

    def __init__(self) -> None:
        self.__items: list = []
        self.__count: int = 0

    def push(self, item: int, digitize=int) -> None:
        """Добавляет в стек"""
        self.__items.append(digitize(item))
        self.__count += 1

    def pop(self) -> int:
        """
        Удаляет и возвращает элемент из стека,
        Если стек пустой - возращает 'error'
        """
        if self.__count == 0:
            raise OperationError('error')
        else:
            self.__count -= 1
            return self.__items.pop()

    @property
    def peek(self) -> int:
        """
        Возвращает последний элемент из стека,
        не удаляя его"""
        return self.__items[-1]

    @property
    def size(self) -> int:
        """
        Возращает размер стека
        """
        return self.__count


def calculate(values: list) -> int:
    """
    Основная логика
    """
    stack = Stack()
    for char in values:
        if char not in OPERATORS:
            stack.push(char)
        else:
            second_number = stack.pop()
            first_number = stack.pop()
            stack.push(getattr(first_number, OPERATORS[char])(second_number))
    return stack.peek


if __name__ == '__main__':
    try:
        print(calculate(input().split()))
    except OperationError as message:
        print(message)
