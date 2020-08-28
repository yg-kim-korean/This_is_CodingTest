import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

#노드 개수 간선 개수 시작 노드 입력받기
n,m,start = map(int,input().split())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n+1)]
#최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선정보 입력받기
for _ in range(m):
    x,y,z = = map(int,input().split())
    #a번 노드에서 b번 노드로 가는 비용이 z라는 의미
    graph[x].append((y,z))

def dijkistra(start):
    q = []
    #시작 노드로 가기위한 최단경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:#q가 비어있지 않으면
        #가장 최단거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] <dist:
            continue
        #현재 노드와 연결되 다른 인접한 노드들을 확인
        for i in graph[now] :
            cost = dist + i[1]
        if cost < distance[i[0]] :
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

dijkistra(start)

#도달할수 있는 노드의 개수
count = 0
#도달할 수 있는 노드중에서, 가장 멀리 있는 노드와의 차단거리
max_distance = 0
for d in distance:
    #도달할 수 있는 노드인 경우
    if d!= INF:
        count+=1
        max_distance = max(max_distance,d)

#시작 노드를 제외해야 하므로 count-1
print(count-1,max_distance)