# ID_1 = 85882520
# ID_2 = 85941877

from exceptions import OperationError

OPERATORS = {'+': '__add__',
             '-': '__sub__',
             '*': '__mul__',
             '/': '__floordiv__'}


def is_operator(operator: str) -> bool:
    """
    Определяет, является ли символ оператором.
    Input: '+'
    Output: True
    """
    if (operator == '+' or operator == '-' or operator == '/'
       or operator == '*'):
        return True
    return False


class Stack:

    def __init__(self) -> None:
        self.items: list = []
        self.count: int = 0

    def push(self, item: int, digitize=int) -> None:
        """Добавляет в стек"""
        self.items.append(digitize(item))
        self.count += 1

    def pop(self) -> int:
        """
        Удаляет и возвращает элемент из стека,
        Если стек пустой - возращает 'error'
        """
        if self.count == 0:
            raise OperationError('error')
        else:
            self.count -= 1
            return self.items.pop()

    @property
    def peek(self) -> int:
        """
        Возвращает последний элемент из стека,
        не удаляя его"""
        return self.items[-1]

    @property
    def size(self) -> int:
        """
        Возращает размер стека
        """
        return self.count


def calculate(values: list) -> int:
    """
    Основная логика
    """
    stack = Stack()
    for char in values:
        if not is_operator(char):
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
