'''
inner class: class within another class is called inner class

'''

class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()


    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'Dell'
            self.processor = 'i5'

        def show(self):
            print("brand %s, processor %s" %(self.brand,self.processor))

s1 = Student('Deepak Noveen',11)
s2 = Student('Dhanasekaran',12)

s1.show()
s2.show()


