'''
Methods are used to perform certain actions, there are three types of methods
Instance methods - Method which uses instance variables
Class methods - Method which uses class variables
Static methods - Method which doesn't use Instance variable or Class variable
'''

class Student():

    school_name = 'DAV matriculation'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        print (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchoolName(cls):
        print cls.school_name

    @staticmethod
    def getInfo():
        print 'This class is 8th standard B section!'

s1 = Student(42,35, 29)
s2 = Student(21,32, 19)

s1.avg()
s2.avg()

Student.getSchoolName()

Student.getInfo()


