arr=[]
n=int(input("Enter the number of elements"))
print("Enter the elements")

for i in range(0,n):
    num=int(input())
    arr.append(num)

r=int(input("Enter number of rotations to be performed"))

for i in range(0,r):
    arr.insert(0,arr.pop())

print(arr)