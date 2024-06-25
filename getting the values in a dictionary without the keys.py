#Example of getting the values in a dictionary without the keys
marks = {
    'Ali': 30, 
    'Sami': 35,
    'Amina ': 28,
    'Aliaa': 20
    }

print (marks)
sum = 0 

for value in marks.values():
	sum += value

print("\nAverage marks is ", sum / len(marks))
