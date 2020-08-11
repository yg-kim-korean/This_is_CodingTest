from collections import deque
n,m  = map(int,input('n m 입력 : ').split())
graph = []
for i in range(n):
    graph.append(list(map(int,input(str(i)+'번째 줄 '+'M 개 만큼 입력 : ').split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    #큐 구현을 위해 디큐 사용
    queue = deque()
    queue.append((x,y))
    #큐가 빌때 까지 반복
    while queue:
        x,y = queue.popleft()
        #현재위치에서 네 방향확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #미로찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue
            #벽인경우 무시
            if graph[nx][ny] ==0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]


print(BFS(0,0))
