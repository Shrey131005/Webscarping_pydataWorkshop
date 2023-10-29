class Employee:
    increament = 2 #calss variable>instance variable
    def __init__(self,fname,lname,salary,age):  #2 underscore
        
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.age  = age
        # self.increament = 5  (instance variable)

    

    def increase(self):
        self.salary = self.salary*Employee.increament # try with *Employee.increament(it will take global variable)
        print(Shrey.salary)
    
   
    @classmethod
    def change_increament(mycalss,amount):
        mycalss.increament = amount

    def __add__(self,other):
        return self.salary + other.salary




Shrey = Employee("Shrey","Patel",5000000,18)
lakshya = Employee("lakshya","saraf",150,18)



# print(Shrey.fname)
# print(Shrey.lname)
# print(Shrey.age)
print(Shrey.salary)
Shrey.increase()
print(Shrey.__dict__)
Employee.change_increament(5.9)
Shrey.increase()
print(Shrey + lakshya)



class encode(Employee):  # inheretence
    def __init__(self,fname,lname,salary,age,laptop,interest):
        super().__init__(fname,lname,salary,age)
        self.interest = interest
        self.laptop = laptop


    
    



