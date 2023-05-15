lowerStr = "abcdefghijklmnopqrstuvwxyz"
upperStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numStr = "0123456789"
otherStr = "!@#$%^&*()_+=-`~[]|:;\"\'<>,.?/"

#https://www.uic.edu/apps/strong-password/

pw = input("Please input your password: ")
point = 0

point += len(pw) * 0.5

for i in range(len(pw)):
    if pw[i] in lowerStr:
        point += 1
    elif pw[i] in upperStr:
        point += 1.2
    elif pw[i] in numStr:
        point += 1.3
    elif pw[i] in otherStr:
        point += 1.5
    else:
        point += 2

print(point)
