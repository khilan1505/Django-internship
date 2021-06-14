# Single level  Inheritance
name = input("Enter name")
designation = input("Enter designation")
salary = input("Enter salary")
class employee():
    
    def details(self,name,designation):
        print(f"Employe Name is {name}")
        print(f"Employe designation is {designation} ")

class subclass(employee):     
       
    def salary(self,salary):
        print(f"Employee salary is {salary}")   
    
display = subclass()
display.details(name,designation)
display.salary(salary)   