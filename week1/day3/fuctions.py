# # # Functions help you reuse code instead of writing the same logic repeatedly.
# # rapido is a cab booking app. We will create a simple program to book a ride using functions.
# # scope means how we are accesing a varible from one function to another function 
# # global scope  and local scope
# # global scope means we can acces any where in our program 
# # local means we can acces only inside that function 

import csv
def rapido_login():
    try:
        name=(input("enter the username:"))
        password=(input("enter the password:"))
        if len(name)<6 or len(password)<6:
            raise ValueError ("username and password must be greater than 6 characters")
        
        return name
    except ValueError as e:
        print("error",e)
        return rapido_login()
        


def book_rapido():
    try:
        current_location=input("enter the current location:")
        destination_location=input("enter the desination location:")

        if current_location == destination_location:
            raise ValueError("current_location and destination_location should not be same")
        return current_location,  destination_location
    

    except ValueError as e:
        print("error ",e)
        return book_rapido()
    

  
def calculate_bill():
    try:
        price_perkm=12
        distance=int(input("input(enter the distance in kms:"))
        discount=int(input("enter the disciunt in percantage:"))
        if distance < 0 or discount < 0:
            raise ValueError("distance or discount is lessthan 0 not accepted")
        else:
            total_bill=distance*price_perkm
            total_bill_with_discount=total_bill-(total_bill*(discount/100))
        return  distance,discount,total_bill,total_bill_with_discount
        
    except ValueError as e:
        print("error",e)
        return calculate_bill()
    


# 4. SAVE TO FILE (FILE HANDLING)
def save_ride(name, current_location,destination_location,distance,discount,total_bill_with_discount):
    with open("rides.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([f"name:{name}, current_location:{current_location},destination:{destination_location},distance:{distance},discount:{discount},total_bill_with_discount:{total_bill_with_discount}"])


# 5. VIEW HISTORY
def view_rides():
    try:
        with open("rides.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    except FileNotFoundError:
        print("No ride history found")


name=rapido_login()
current_location,destination_location=book_rapido()
distance,discount,toltal_bill,total_bill_with_discount=calculate_bill()
save_ride(name, current_location,destination_location,distance,discount,total_bill_with_discount)
view_rides()




# def rapido():
#     name = input("enter your name: ")

#     "docstring: this function is used to get the name of the user"

#     return name


# def places():
#     print("you an select places to go")
#     "docstring: this function shows the available places"
#     print(1, "hyderbad")
#     print(2, "banglore")
#     print(3, "chennai")
#     print(4,"delhi")


# def book_ride():
#     "docstring :this function is used to book a ride and get the place and distance from the user"
#     place=input("enter the place you want to go: ")
#     distance=int(input("enter the distance: "))
#     return place,distance
    
# def total_bill(distance):
#     price_perkm=10
#     discount=int(input("enter the discount percentage: "))
#     total=distance*price_perkm
#     total1=total*(discount/100)
#     "docstring: this function is used to calculate the total bill"
#     return total1

# user=rapido()
# places()
# place,distance=book_ride()
# bill=total_bill(distance)
# print("total price of the bill:", bill)
# print(f"User: {user}, Place: {place}, Bill: {bill}")


# # accesing a varible from one function to another function is called scope

# st="naveen"
# def func():
#     print(st)
# func()
#  # the variable st is global scopw we can acces it any where in ouur program



# def func1():
#     st1="reddy"
# func1()
# print(st1)

# # this shows an error because st1 is a local scope we cannot acces it out side fuction 


# mini style rapido app which covers functions and scope and docstring expection handling and and csv files 
