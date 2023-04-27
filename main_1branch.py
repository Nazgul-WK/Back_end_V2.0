class Calculator:
    def __init__(self, a: int, b: int ):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    def diff(self):
        return self.a - self.b
    def sub(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b