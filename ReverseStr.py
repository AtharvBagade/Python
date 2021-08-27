def ReverseString(str):
     if len(str)==0:
         return str
        
     else :
        return ReverseString(str[1:])+str[0]


Mystr= input('Enter a string')

print('The given string is :'+Mystr)
print('The given string is :'+ReverseString(Mystr))
