num=int(input("Enter a number"))
count=0

for i in range(1,num-1):
    if num%i==0:
       count=count+i 

if count==num:
     print("It's a perfect number")

else: 
    print("Not a perfect number")


      

