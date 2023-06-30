lowerStr = "abcdefghijklmnopqrstuvwxyz"
upperStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numStr = "0123456789"
otherStr = "!@#$%^&*()_+=-`~[]|:;\"\'<>,.?/"

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

# https://www.uic.edu/apps/strong-password/

# 문자 수 Number of characters
point += len(pw) * 4
# 전체 - 대문자 수 Uppercase letters
point += (len(pw) - upper) * 2
# 전체 - 소문자 수 Lowercase Letters
point += (len(pw) - lower) * 2
# 숫자 Numbers
point += num * 4
# 특수 문자 Symbols
point += other * 6

# 처음 끝을 제외한 곳의 특수 문자 Middle numbers or symbols
for j in range(len(pw) - 2):
    for i in range(len(numStr)):
        if (pw[j+1] == numStr[i]):
            point += 2
    for i in range(len(otherStr)):
        if (pw[j+1] == otherStr[i]):
            point += 2

# 조건 충족 Requirements
# 8자 이상, 대문자, 소문자, 숫자, 특수문자 포함
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

print(point)

if point >= 80:
    print("Very Strong")
elif point >= 60:
    print("Strong")
elif point >= 40:
    print("Weak")
else:
    print("Very Weak")