n,m = map(int,input('N M 입력 : ').split())
leng = []

for i in range(n):
    leng.append(list(map(int,input(str(i+1)+'번째 줄 '+str(m)+'개 입력 : ').split())))

result = 0
for i in range(n):
    temp = min(leng[i])
    result = max(result,temp)

print(result)