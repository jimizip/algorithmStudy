A,B,C = map(int, input().split())
if A == B == C:
    print(10000+A*1000)
elif A == B or A == C or B == C:
    if A == B or A == C:
        print(1000+A*100)
    else:
        print(1000+B*100)
else:
   print(100*max(A,B,C))

# max
    