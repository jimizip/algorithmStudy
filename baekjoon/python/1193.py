X = int(input())
line = 1

while X > line:
    X -= line
    line+=1

if line % 2 == 0:
    up = X
    down = line - X + 1
elif line % 2 == 1:
    up = line - X + 1
    down = X

print(up, "/", down, sep="")