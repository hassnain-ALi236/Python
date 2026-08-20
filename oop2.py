# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def Area(self):
#         result=3.14*(self.radius**2)
#         return(result)
#     def parameter(self):
#         result=2*3.14*self.radius
#         return result
# c1=circle(21)
# print(c1.radius)
# print(c1.Area())
# print(c1.parameter())

class Emp:
    def __init__(self,role,dep,salary):
        self.role=role
        self.dep=dep
        self.salary=salary
    def showDetails(self):
        print("Your Detail is given as--> " ,self.role,self.dep,self.salary,self.age,self.name)
class eng(Emp):
    def __init__(self,name,age,dep,salary,role):
        self.name=name
        self.age=age
        super().__init__(role,dep,salary)
en1=eng("Hassnain",19,"Science",85000,"Senior Manager")
print(en1.name)
en1.showDetails()