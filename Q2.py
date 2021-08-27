fname=input("Enter a filename")
char=input("Enter a letter")

def letterFrequency(fileName, letter):
    file = open(fileName, 'r')
    text = file.read()
    return text.count(letter)
print(letterFrequency(fname, char))