f = open("C:/Users/user/PycharmProjects/pythonProject/NimGame/main.py",'r')
nline = 0
nchar = 0
nwords = 0
nspaces = 0
for line in f:
    nline += 1
    nchar += len(line)
    nwords += len(line.split())
    for c in line:
        if c.isspace():
            nspaces += 1
print("Number of words: ", nwords)
print("Number of lines: ", nline)
print("Number of characters: ", nchar)
print("Number of characters without spaces: ", (nchar-nspaces))
print("Number of spaces: ", nspaces)
print("Number of new lines: ", (nline-1))