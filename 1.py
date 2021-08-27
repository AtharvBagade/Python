#variable
x=10

#data types
#integer
x=10

#float
x=10.5

#string
x="Good morning"

#character
x="C"

#arraylist
array=[1,2,3,4,5]
#posi= 0 1 2 3 4

#dictionary
d=dict()
#key values pairs
# key1=value1 eg one=1 or 1=one 

#get integer input from user
#global variables
number1=int(input("Enter a number"))   
number2=int(input("Enter a number"))   
 

#function1 with parameters
#parameters are numbers or variables taken from the user
def addition(num1,num2):
     #local variable
     add=num1+num2
     return add
     
#function2
def subtraction(num1,num2):
     return num1-num2

add1=addition(number1,number2)


#Output of the program
print(add1)
print(subtraction(number1,number2))
