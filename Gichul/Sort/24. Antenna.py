#정렬
n = int(input())
data = list(map(int,input().split()))
data.sort()

print(data[(n-1)//2])

#중간값;;