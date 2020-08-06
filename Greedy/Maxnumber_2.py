n,m,k = map(int,input('3개 입력 : ').split())
data = list(map(int,input('n개 입력 : ').split()))

data.sort()
f = data[n-1]
s = data[n-2]
result = 0

count = int(m/(k+1))*k
count+= m%(k+1)

result = count*f
result+=(m-count)*s
print(result)
