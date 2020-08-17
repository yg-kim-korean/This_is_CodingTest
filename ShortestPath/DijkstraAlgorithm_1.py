#1. 출발노드 선정
#2. 최단거리 테이블을 초기화
#3. 방문하지 않은 노드중에서 최단거리가 가장 짧은 노드를 선택
#4. 해당노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단거리 테이블을 갱신
#5. 위 과정에서 3,4 반복

#구현방법
#1. 구현하기 쉽지만 느리게 동작하는 코드

import sys
input = sys.stdin.readline
INF = int(1e9)
#노드/간선의 개수 입력받기
n,m = map(int,input().split())
#시작노드입력받기
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
#방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)
#모든 간선 정보를 입력받기.
for _ in range(m):
    a,b,c = map(int,input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

#방문하지 않은 노드중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 #가장 최단거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        #현재 최단거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smallest_node()
        visited[now] = True
        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost= distance[now]+j[+1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)
#모든 노드로 가기위한 최단거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] ==INF:
        print("Infinity")
    else:
        print(distance[i])
