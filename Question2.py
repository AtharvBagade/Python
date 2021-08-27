arr=[]

n=int(input("Enter the length of the array"))

print("Enter the elements")

for i in range(0,n):
     num=int(input())
     arr.append(num)

def Search(arr):
    for i in range(0, len(arr)):    
     for j in range(i+1, len(arr)):  
        if(arr[i]==arr[j]):
            return False


def Increment(arr):

  for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        while(arr[i] == arr[j]):
           arr[j]=arr[j]+1


while Search(arr)==False:

     Increment(arr)

print(arr)
print(sum(arr))
