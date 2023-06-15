from exception_new import TriangleError
"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с
суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с
такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или
равносторонним.
"""

'Задание 1 из Домашнего задания 1'
a = int(input("Введите первую сторону: "))
b = int(input("Введите вторую сторону: "))
c = int(input("Введите третью сторону: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Треугольник равносторонний")
    elif a == b or b == c or a == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    raise TriangleError(a, b, c)