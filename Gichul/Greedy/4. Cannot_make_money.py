#그리디
n = int(input())
l = list(map(int,input().split()))
l.sort()
target = 1
for x in l:
    #만들수 없는 금액을 찾았을때 반복종료
    if target < x:
        break
    target+=x


print(target)

