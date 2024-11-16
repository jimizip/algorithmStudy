
N = int(input())
for i in range(1, 1+N):
    str_num = str(i)
    count_369 = str_num.count('3') + str_num.count('6') + str_num.count('9')
    
    if count_369 > 0:
        print('-' * count_369, end=' ')
    else:
        print(str_num, end=' ')