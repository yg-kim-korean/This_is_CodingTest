from collections import deque
import copy

#노드 개수 입력받기
v = int(input())
#모든 노드의 진입차수는 0으로 초기화
indegree = [0] * (v+1)
#각 노드에 연결된 간선 정보를 담기위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]
#각 강의 시간을 0으로 초기화
time = [0] * (v+1)

#방향 그래프의 모든 간선정보를 입력받기
for i in range(1,v+1):
    data = list(map(int,input().split()))
    time[i] = data[0] #첫번쨰는 시간 정보
    for x in data[1:-1]:
        indegree[x] -=1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time) #알고리즘 수행 결과를 담을 리스트
    q = deque()

    #처음시작할 때는 진입차수가 0인 노드로 시작
    for i in range(1,v+1):
        if indegree[i] ==0:
            q.append(i)

    while q:
        #큐에서 원소 꺼내기
        now = q.popleft()
        #해당원소와 연결된노드들의 진입차수에서 1빼기
        for i in graph[now]:
            result[i] = max(result[i],result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이되는 노드를 큐에 삽입
            if indegree[i] ==0:
                q.append(i)

        for i in range(1,v+1):
            print(result[i])

topology_sort()

