word_table = []
res = ''
max_len = []
for _ in range(5):
    word = input()
    word_table.append(word)
    max_len.append(len(word))

for i in range(max(max_len)):
    for j in range(5):
        if i < len(word_table[j]):
            print(word_table[j][i], end='')
