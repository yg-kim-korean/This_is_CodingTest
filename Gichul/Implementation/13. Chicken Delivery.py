#구현
#삼성
from itertools import combinations
n,m = map(int,input().split())
house = []
chicken = []

for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append([i,j])
        elif data[j] == 2:
            chicken.append([i,j])

#모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken,m))

def get_sum(candidate):
    result = 0
    #모든 집에 대하여
    for hx,hy in house:
        #가장 가까운 치킨집 찾기
        temp = 1e9
        for cx,cy in candidate:
            temp = min(temp,abs(hx-cx)+abs(hy-cy))
        #가장 가까운 치킨집까지의 거리를 더하기
        result+=temp
    #치킨 거리의 합 반환
    return result

#치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result,get_sum(candidate))

print(result)
