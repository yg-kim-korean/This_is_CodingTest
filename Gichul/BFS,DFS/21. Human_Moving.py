#bfs, dfs
from collections import deque

#땅의 크기 (n),L,R값 받기
n,l,r = map(int,input().split())

#전체나라의 정보를 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

result = 0

#특정위치에서 출발하여 모든 연합을 체크한뒤에 데이터 갱신
def process(x,y,index):
    #(x,y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x,y))
    #너비우선 탐색(BFS)를 위한 큐 자료구조 정의
    q = deque()
    q.append((x,y))
    union[x][y] = index #현재 연합의 번호 할당
    summary = graph[x][y]# 현재 연합의 전체 인구 수
    count = 1 #현재연합의 국가 수
    #큐가 빌때까지 반복(BFS)
    while q:
        x,y = q.popleft()
        #현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #바로 옆에 있는 나라를 확인하여
            if 0<=nx and nx < n and 0<= ny and ny <n and union[nx][ny]==-1:
                #옆에 있는 나라와 인구차이가 L명이상 R명 이하라면
                if l<= abs(graph[nx][ny]-graph[x][y]) <= r:
                    q.append((nx,ny))
                    #연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count+=1
                    united.append((nx,ny))
    #연합인구끼리 인구 분배
    for i,j in united:
        graph[i][j] = summary//count
    return count

total_count = 0

#더이상 인구이동을 할 수 없을때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1 :
                process(i,j,index)
                index+=1
    #모든 인구 이동이 끝난경우
    if index ==n *n:
        break
    total_count+=1

#인구 이동횟수 출력
print(total_count)



