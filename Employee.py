class Person:
    
     def __init__(self,per_name,per_address):
      self.name= per_name
      self.address=per_address

class Employee(Person):
    def __init__(self ,emp_name,emp_address,emp_salary,emp_staffid):
        self.salary=emp_salary
        self.staffid=emp_staffid
        Person.__init__(self,emp_name,emp_address)

emp1=Employee("John","Aundh",15000,"a1")
emp2=Employee("Robert","Pune City",15000,"a2")
emp3=Employee("Dizzy","Baner",13000,"b1")

print("name:",emp1.name,"address:",emp1.address,"salary:",emp1.salary,"staffID:",emp1.staffid)
print("name:",emp2.name,"address:",emp2.address,"salary:",emp2.salary,"staffID:",emp2.staffid)
print("name:",emp3.name,"address:",emp3.address,"salary:",emp3.salary,"staffID:",emp3.staffid)


