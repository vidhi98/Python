from math import sqrt
num=input()
f = [1]
sq = int(sqrt(num))
for i in range(2, sq):
    if num % i == 0:
            f.append(i)
            f.append(num/i)
    if sq > 1 and num % sq == 0:
        f.append(sq)
        if sq*sq != num:
            f.append(num/sq)
    print(f)
