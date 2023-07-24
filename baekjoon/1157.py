word = input().upper()
word_list = list(set(word))
count_list = [word.count(i) for i in word_list]

if count_list.count(max(count_list)):
    print("?")
else:
    print(word_list[count_list.index(max(count_list))])