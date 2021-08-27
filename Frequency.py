all_freq = {}
a = input('enter a string')

def freq(test_str):
   for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

freq(a)

print ('Count of all characters in',a,' is :\n ' + str(all_freq))

