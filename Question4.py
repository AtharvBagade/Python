a=int(input("Enter a"))
b=int(input("Enter b"))

x=a
y=b

while(x!=y):
    if(x>y):
        x=x-y
    
    elif(y>x):
        y=y-x

print(x)
print(y)