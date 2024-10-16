t = int(input())

for test in range(1, t+1):
    l = map(int, input().split())
    s = 0
    for i in l:
        if(i % 2 != 0):
            s += i
    print("#"+str(test), str(s))