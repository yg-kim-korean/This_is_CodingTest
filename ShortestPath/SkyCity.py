#플로이드 워셜 사용
INF = int(1e9)

#노드의 개수 및 간선의 개수를 입력
n,m = map(int,input().split())
#2차원 리스트(그래프 표현) 만들고, 모든값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에게는 0으로 초기화
for a in range(n+1):
    for b in range(n+1):
        if a==b:
            graph[a][b]= 0

#간선정보 입력
for _in range(m):
    #A와 B가 서로에게 가는 비용은 1이라고 설정
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

#거쳐갈 노드 X와 최종목적지 k입력
x,k = map(int,input().split())

#점화식에 따라 플로이드 워셜
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] +graph[k][a])

#결과 출력
distance = graph[1][k] + graph[k][x]   #틀린거 아님?


#결과 출력

if distance >= INF:
    print("-1",end=' ')
else:
    print(distance)
