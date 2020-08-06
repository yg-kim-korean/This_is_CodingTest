n,m,k = map(int,input('3개 입력:').split())
data = list(map(int,input('n개 입력').split()))

data.sort()
f = data[n-1]
s = data[n-2]
result = 0
while True:
    for i in range(k):
        if m==0:
            break
        result+=f
        m-=1
    if m==0:
        break
    result +=s
    m-=1
print(result)

