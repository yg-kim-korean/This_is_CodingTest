#구현
n = input()
x = len(n)//2
result1= 0
result2=0
for i in range(len(n)):
    if i <= x-1:
        result1 += int(n[i])
    else:
        result2 += int(n[i])


if result1 ==result2:
    print("LUCKY")
else:
    print("READY")