class A():
    def __init__(self):
        print ('Inside init A')

    def feature1(self):
        print ('I am feature1')

    def feature2(self):
        print ('I am feature2')

class B:

    def __init__(self):
        print ('Inside init B')

    def feature3(self):
        print ('I am feature3')

    def feature4(self):
        print ('I am feature4')

#single level inhertance
class C(A):

    def __init__(self):
        super(A,self).__init__()
        print ('Inside init C')

    def feature5(self):
        print ('I am feature5')

    def feature6(self):
        print ('I am feature6')

c1 = C()
