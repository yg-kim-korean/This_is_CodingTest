#그리디
n = int(input())
guys = list(map(int,input().split()))

guys.sort()


result = 0 #총 그룹수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in guys:
    count+=1
    if count >=i:
        result+=1
        count=0

print(count)