#  File: Employee.py
#  Student Name: Ramsay Ward
#  Student UT EID:rjw2777



class Employee:

    def __init__(self, name, id, salary = None, **kwargs):
      
#initializing my name is and salary 
      self._name = name
      self._id = id
      self._salary = salary
      
      

#get salary function 
    def get_salary(self):
        return self._salary

#set salary function
    def set_salary(self, salary):
        self._salary = salary
        
#get name function
    @property
    def name(self):
        return self._name
        
        
#get id function 
    @property
    def id(self):
        return self._id

    def __str__(self):
        return f"{self.name}, {self.id}, {self._salary}"
    







############################################################
############################################################
############################################################
class Permanent_Employee(Employee):
    def __init__(self, benefits, **kwargs):
        Employee.__init__(self,**kwargs)
        
        
        self._benefits = benefits
        
        
        
  
    @property
    def benefits(self):
        
        return (self._benefits)
      
    @benefits.setter
    def benefits(self, benefits):
        
        self._benefits = benefits
       
        
        
        

    def cal_salary(self):
        
        if self._benefits == ['health_insurance']:
            return (self._salary*.9)
        
        if self._benefits == ['retirement']:
            return (self._salary*.8)
        else:
            return (self._salary*.7)
            
        
    
        
       
            
    def __str__(self):
        return f"{self.name}, {self.id}, {self._salary}, {self.benefits}"




############################################################
############################################################
############################################################
class Manager(Employee):
    def __init__(self, bonus, **kwargs):
        Employee.__init__(self,**kwargs)
        
        self._bonus = bonus

    def cal_salary(self):
         return float (self._bonus + self._salary)

    @property
    def bonus(self):
        return self._bonus

    def __str__(self):
        return f"{self._name}, {self.id}, {self._salary}, {self.bonus}"
    
    
    



############################################################
############################################################
############################################################
class Temporary_Employee(Employee):
    def __init__(self, hours, **kwargs):
        Employee.__init__(self, **kwargs)
        #super().__init__(**kwargs)
        self._hours  = hours

            
        

    def cal_salary(self, **kwargs):
        return float (self._hours * self._salary)
        

    def __str__(self):
        return f"{self._name}, {self.id}, {self._salary}, {self._hours}"






############################################################
############################################################
############################################################
class Consultant(Temporary_Employee):
    
        
    def __init__(self, travel, **kwargs):
    
        Temporary_Employee.__init__(self,**kwargs)
        self.travel = travel
    

    def cal_salary(self):
        return float (self._salary * self._hours) + (self.travel *1000)

    def __str__(self):
        return f"{self._name}, {self.id}, {self._salary}, {self._hours}, {self.travel}"



############################################################
############################################################
############################################################
class Consultant_Manager(Consultant, Manager):
    def __init__(self,  **kwargs):
        Consultant.__init__(self, **kwargs)
        
        Manager.__init__(self,**kwargs)
        

    def cal_salary(self):
        return float((self._salary * self._hours) + ( self.travel * 1000) + self.bonus)

    def __str__(self):
        return f"{self.name}, {self.id}, {self._salary}, {self._hours}, {self.travel}, {self.bonus}"


''' ##### DRIVER CODE #####
    ##### Do not change. '''

def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())

    print("Sam's Salary is:", sam.cal_salary())

    print("John's Salary is:", john.cal_salary())

    print("Charlotte's Salary is:", charlotte.cal_salary())

    print("Matt's Salary is:",  matt.cal_salary())


if __name__ == "__main__":
    main()
