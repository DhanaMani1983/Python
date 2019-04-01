'''
An object is a type which we need to do something, for example: to write programming
we need laptop object, Human is an object which has attributes like height, weight, colour etc
and behaviours like walking, talking etc

Here attributes are called properties and behaviours are called methods in programming language

To do recording we need camera object

Class is a design/template which intiates an object, object is an instance of a class.

Using a class you can create multiple objects
'''

class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Config is %s, %s' %(self.cpu, self.ram))


comp = Computer('i5','16gb')
comp.config()

comp1 = Computer('razen3','64gb')
comp1.config()




