f = open("C:/Users/user/PycharmProjects/pythonProject/hangman_game/main.py",'r')
words_list = []
for line in f:
    for word in line.split():
        words_list.append(word)
print(words_list)
f.close()