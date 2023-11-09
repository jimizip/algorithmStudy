import sys

word = sys.stdin.readline().split()
word_list = []
for i in word:
    word_list.append(i)
print(len(word_list))