import os
fname = input("Enter file name: ")

file_stats = os.stat(fname)

print(file_stats)
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')

textfile = open(fname)
lines = textfile.readlines()
for line in reversed(lines):
    print(line)

textfile.close()