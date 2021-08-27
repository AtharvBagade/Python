def Recur_factorial(n):
     if n==0:
         return 1
     
     elif n==1:
        return n
    
      
     else:
         return n*Recur_factorial(n-1)

num=int(input('Enter a number'))

if(num < 0):
    print('Sorry,factorial does not exist for negative numbers')

else:
  print('The factorial of ',num,'is ',Recur_factorial(num))



  
    
