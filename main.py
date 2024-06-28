# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.get_square() == other.get_square()
#         return False
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             new_square = self.get_square() + other.get_square()
#             new_height = self.height
#             new_width = new_square / new_height
#             return Rectangle(new_width, new_height)
#         return NotImplemented
#
#     def __mul__(self, n):
#         if isinstance(n, (int, float)):
#             new_width = self.width * n
#             new_height = self.height * n
#             return Rectangle(new_width, new_height)
#         return NotImplemented
#
#     def __str__(self):
#         return f'Rectangle(width={self.width}, height={self.height})'
#
#     def __hash__(self):
#         return hash((self.width, self.height))
#
#
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
#
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 26, 'Test3'
#
# r4 = r1 * 4
# assert r4.get_square() == 128, 'Test4'
#
# assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
#
# print(r1)  # Rectangle(width=2, height=4)
# print(r2)  # Rectangle(width=3, height=6)
# print(r3)  # Rectangle(width=6.5, height=4)
# print(r4)  # Rectangle(width=8, height=16)


import math

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        self.a = a
        self.b = b
        self.reduce()

    def reduce(self):
        gcd = math.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.a
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.b + other.a * self.b
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.b - other.a * self.b
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a == other.a and self.b == other.b
        return False

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > other.a * self.b
        return False

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < other.a * self.b
        return False

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

# Тестування
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 7, 6', f"Expected 'Fraction: 7, 6', but got {str(f_c)}"
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 1, 3', f"Expected 'Fraction: 1, 3', but got {str(f_d)}"
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6', f"Expected 'Fraction: 1, 6', but got {str(f_e)}"

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')

