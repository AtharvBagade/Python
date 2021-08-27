s=input()
new_str=""
for i in range (len(s)):
    if s[i].isupper():
        new_str+=s[i].lower()
    elif s[i].islower():
        new_str+=s[i].upper()
    else:
        new_str+=s[i]
print(new_str)
        with open("test.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)