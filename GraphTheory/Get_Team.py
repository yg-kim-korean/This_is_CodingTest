#전형적인 서로소 문제

#특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    #루트 찾을때까지
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int,input().split())
parent = [0] * (n+1) #부모테이블 초기화

#부모테이블에 일단 자기 자신을 루트로 만들기
for i in range(n+1):
    parent[i] = i

#각 연산을 하나씩 하기
for i in range(m):
    oper, a, b = map(int,input().split())
    #합집합연산일 경우
    if oper ==0:
        union_parent(parent,a,b)
    else:
        if find_parent(parent,a) == find_parent(parent,b):
            print('Yes')
        else:
            print('No')