#DFS 사용
n,m = map(int,input('N M 값 입력 : ').split())

graph = []
for i in range(n):
    graph.append(list(map(int,input(str(i)+'번째 줄 '+'M 개 만큼 입력 : ').split())))

# DFS로 특정한 노르를 방문한 뒤에 연결된 모든 노드들도 방문
def DFS(x,y):
    #주어진 범위가 벗어나면 즉시 종료
    if x<= -1 or x >= n or y <=-1 or y >= m:
        return False
    #현재 노드를 방문하지 않았으면
    if graph[x][y] == 0:
        #현재노드 방문처리
        graph[x][y] = 1
        #상 하 좌 우 위치도 모두 재귀로 호출
        DFS(x-1,y)
        DFS(x,y-1)
        DFS(x+1,y)
        DFS(x,y+1)
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        #현재위치에서 재귀 수행
        if DFS(i,j) == True:
            result +=1
print(result)