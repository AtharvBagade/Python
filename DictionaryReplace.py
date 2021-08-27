n=int(input('Enter n'))
d=dict()

for x in range(1,n+1):
      d[x]=x*x

      key=int(input("Enter key to check:"))
      if key in d.keys():
            value=int(input('Key is present enter a new value to replace'))
            d[key]=value
            print(d)
      
      else:
            print("Key isn't present!")