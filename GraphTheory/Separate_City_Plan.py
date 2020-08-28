#크루스칼 알고리즘을 통해 최소신장트리 구한다음 
#가장 비용이 큰 구간을 없애서 2 집합으로 나눈다


def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int,input().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1,v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int,input().split())
    #비용순으로 정렬하기위해 비용을 맨앞으로
    edges.append((cost,a,b))

edges.sort()
last = 0 #최소 신장 트리에서 포함되는 간선중에서 가장 비용이 큰 간선

for edge in edges:
    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
        last = cost

print(result-last)