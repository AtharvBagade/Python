holes=0

number=3689

n=str(number)

 
for i in n:
    if i=='0' or i=='4' or i=='6' or i=='9':
        holes=holes+1

    elif i=='8':
        holes=holes+2

print(holes)


    