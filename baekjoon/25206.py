grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
level = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F", "P"]
major = 0
total = 0

for _ in range(20):
    n,g,l = input().split()
    g = float(g)
    if l != "P":
      major += (g*grade[level.index(l)])
      total += g
print('%.6f' % (major/total))