class FileException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'У вас отсутствует обязательный параметр {self.value}.'


class TriangleError(Exception):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольника со сторонами {self.a}, {self.b} и {self.c} не существует.'
