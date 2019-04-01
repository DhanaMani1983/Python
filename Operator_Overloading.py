'''
you can create overload methods for operators
'''


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m3 = self.m1 + other.m1
        m4 = self.m2 + other.m2

        s = Student(m3, m4)
        return s


s1 = Student(24,34)
s2 = Student(45,23)

s3 = s1 + s2

print(s3.m1, s3.m2)