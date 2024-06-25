# Example on files
f = open("file", encoding='utf-8')  # File should exist
for line in f:
    print(line)
print('\n')
f.seek(0)
for line in f:
    print(line, end='')
print('\n')
lst = []
f.seek(0)
for line in f:
    for word in line.split():
        lst.append(word)
print(lst)
f.close()
x = input('Press enter to finish')
