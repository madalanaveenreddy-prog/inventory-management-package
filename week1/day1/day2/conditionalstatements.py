# implement control flow using conditions and loops
# we can use if statements to execute a block of code only if a certain condition is true
x = 10
if x > 5: 
    print("x is greater than 5")    
# we can use else statements to execute a block of code if the condition is false
if x > 15:
    print("x is greater than 15")
else:    print("x is not greater than 15")  
# we can use elif statements to check multiple conditions
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:    print("x is not greater than 5")       
# we can use nested if statements to check for multiple conditions
if x > 5:
    if x > 15:
        print("x is greater than 15")
    else:        print("x is greater than 5 but not greater than 15")    
else:    print("x is not greater than 5")
# we can use for loops to iterate over a sequence of items
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:  
    print(fruit)
# we can use while loops to execute a block of code as long as a certain condition is true
count = 0
while count < 5:
    print(count)
    count += 1          
    # we can use break statements to exit a loop early
for i in range(10):
    if i == 5:
        break
    print(i)
# we can use continue statements to skip the rest of the current iteration and move on to the next iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)        
    # we can use the pass statement as a placeholder for code that we haven't written yet
for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)        
# we can use the else clause with loops to execute a block of code after the loop has finished, but only if the loop was not terminated by a break statement
for i in range(5):
    print(i)
else:    print("Loop finished without break")
for i in range(5):
    if i == 3:
        break
    print(i)
else:    print("Loop finished without break")

    