class OperationError(Exception):
    """Выбрасывается, когда невозможно сделать операцию"""

    def __init__(self, text='error'):
        self.text = text
