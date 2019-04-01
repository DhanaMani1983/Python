'''
Inheritcnce - Super class is the parent class, Child class inherits from base class or super class all its attributes and methods

Single Inheritance
Multi level Inheritance
Multiple Inheritance
'''

class A:
    def feature1(self):
        print ('I am feature1')

    def feature2(self):
        print ('I am feature2')

class B:
    def feature3(self):
        print ('I am feature3')

    def feature4(self):
        print ('I am feature4')

#single level inhertance
class C(A):
    def feature5(self):
        print ('I am feature5')

    def feature6(self):
        print ('I am feature6')

#multi level inheritance
class D(C):
    def feature7(self):
        print ('I am feature7')

    def feature8(self):
        print ('I am feature8')

#multiple level inheritsance
class E(B,D):
    def feature9(self):
        print ('I am feature9')

    def feature10(self):
        print ('I am feature10')

