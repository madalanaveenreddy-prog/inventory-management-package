# li=["naveen",1,4,9.4,"python"]
# for i in range(len(li)):
#     print(li[i])

# def function():

#     # Variables
#     name = "Naveen"
#     age = 50
#     gpa = 9.4

#     # Print values
#     print("Name:", name)
#     print("Age:", age)
#     print("GPA:", gpa)

# # Function Call
# function()



# class person:
#     def __init__(self, name, age, grade):
#         self.grade = grade
#         self.name = name
#         self.age = age

# class bigperson(person):
#     def __init__(self, name, age, grade, marks):
#         super().__init__(name, age, grade)
#         self.marks = marks

# student = bigperson("naveen", 23, 4.5, 85)
# print(student.name)
# print(student.age)
# print(student.grade)
# print(student.marks)


# li=[1,2,3,4,5,6]
# count=0
# for  i in range(len(li)):
#     count=count+li[i]
# print(count)



# # employee management system


# class employee:
#     def __init__(self ,name,age,department,salary):
#         self.name=name
#         self.age=age
#         self.department=department
#         self.salary=salary
#     def show_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Department:", self.department)
#         print("Salary:", self.salary)
# display=employee("naveen",23,"IT",50000)
# display.show_details()


# def function():
#     name="naveen",
#     age=23,
#     department="IT",
#     salary=50000
#     print("Name:", name)
#     print("Age:", age)
#     print("Department:", department)
#     print("Salary:", salary)
#     li=[123,456,789]
#     for i in li:
#         print(i)
#     dic={"name":"naveen","age":23,"department":"IT","salary":50000}
#     for key,values in dic.items():
#         print(key,values)

# function()



class bank():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    def withdraw(self,amount):
        self.balance=self.balance-amount
        return self.balance
    def show(self):
        return self.name,self.balance
bank1=bank("naveen",50000)
bank1.deposit(60000)
bank1.withdraw(20000)
print(bank1.withdraw)
print(bank1.balance)
bank1.show()

def atm():
    # variables
    atm_name="sbi"
    atm_location="hyderabad",
    print("ATM Name:", atm_name)
    print("ATM Location:", atm_location)
    
# list  
    options=["deposit","withdraw","checkbalance"]   
    for i in options:
       print(i)

# tuple
    timings=("9am","5pm")
    for i in timings:
        print(i)

#dictionaries
    notes={100:100000,200:200000,300:300000}
    for key,values in notes.items():
       print(key,values)

atm()
bank1=bank("naveen",50000)
bank1.deposit(10000)
bank1.withdraw(20000)
print(bank1.withdraw)
print(bank1.balance)
bank1.show()












atm()

    