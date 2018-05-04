class Student:
    def __init__(self,name,age,dob,gender):
        self.name=name
        self.age=age
        self.dob=dob
        self.gender=gender

    def display(self):
        print("welcome %s! your are a %s your Date of Birth is: %s your age is:%d" %(self.name,self.gender,self.dob,self.age))


s=Student("Dhanasekaran Mani",35,"21/06/1983","Male")
s.display()