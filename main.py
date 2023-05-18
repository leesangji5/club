lowerStr = "abcdefghijklmnopqrstuvwxyz"
upperStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numStr = "0123456789"
otherStr = "!@#$%^&*()_+=-`~[]|:;\"\'<>,.?/"

#20p vw
#4op w
#60p s
#80p vs


pw = input("Please input your password: ")
point = 0

upper = 0
for i in range(len(pw)):
    if pw[i] in upperStr:
        upper += 1
lower = 0
for i in range(len(pw)):
    if pw[i] in lowerStr:
        lower += 1
other = 0
for i in range(len(pw)):
    if pw[i] in otherStr:
        other += 1
num = 0
for i in range(len(pw)):
    if pw[i] in numStr:
        num += 1

point += len(pw) * 4
point += (len(pw) - upper) * 2
point += (len(pw) - lower) * 2
if (upper + lower + other) != 0:
    point += num * 4
point += other * 6

if len(pw) >= 8:
    point += 2
if upper != 0:
    point += 2
if lower != 0:
    point += 2
if num != 0:
    point += 2
if other != 0:
    point += 2

print(pw[2])
print(numStr[2])
print(otherStr[2])

for j in range(len(pw) - 2):
    for i in range(len(numStr)):
        if (pw[j+1] == numStr[i]):
            point += 2
    for i in range(len(otherStr)):
        if (pw[j+1] == otherStr[i]):
            point += 2


print(point)
