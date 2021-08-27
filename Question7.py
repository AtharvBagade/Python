string=input("Enter the string")


def Most_Duplicate_Character(str1):
    
    count = 0
     
    for i in str1:
        count2 = str1.count(i)
        if(count2 > count):
            count = count2
            num = i
 
    print(num,"Count:",count)
 
Most_Duplicate_Character(string)
