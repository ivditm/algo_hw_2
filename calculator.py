# ID = 85882520

import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO)


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
        self.items = []
        self.count = 0

    def push(self, item: int) -> None:
        """Добавляет в стек"""
        self.items.append(item)
        self.count += 1

    def pop(self):
        """
        Удаляет и возвращает элемент из стека,
        Если стек пустой - возращает 'error'
        """
        if self.count == 0:
            return 'error'
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
            logging.debug(char)
            stack.push(int(char))
        else:
            second_number = stack.pop()
            first_number = stack.pop()
            logging.debug(first_number, second_number)
            if char == '*':
                stack.push(second_number * first_number)
            elif char == '+':
                stack.push(first_number + second_number)
            elif char == '-':
                stack.push(first_number - second_number)
            else:
                stack.push(first_number // second_number)
    return stack.peek


if __name__ == '__main__':
    print(calculate(input().split()))
