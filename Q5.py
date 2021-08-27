filename=input("Enter a filename:")

def file_read_from_head(fname, nlines):
                        from itertools import islice
                        with open(fname) as f:
                                for line in islice(f, nlines):
                                        print(line)
file_read_from_head(filename,2)

def read_lastnlines(fname,n):
                        with open(filename) as f:
                                for line in (f.readlines() [-n:]):
                                        print(line)

read_lastnlines(filename,3)