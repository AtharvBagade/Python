arr=[]
n=int(input("Enter the length of list:"))
print("Enter the elements")

for i in range(0,n):
    num=int(input())
    arr.append(num)


def findsublist(arr):
 
    for i in range(len(arr)):
        sum = 0
      
        for j in range(i, len(arr)):
            
            sum += arr[j]
            
            if sum == 0:
                print(arr[i:j+1])
 

findsublist(arr)
 