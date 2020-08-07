n = int(input('몇칸짜리 ? : '))
go = input('어떻게 갈래 ? : ').split()
result = [0,0]
for i in go:
    if i == 'R':
        if result[1] < n-1:
            result[1] +=1
    elif i == 'L':
        if result[1] > 0:
            result[1] -=1
    elif i == 'U':
        if result[0] > 0:
            result[0] -=1
    else:
        if result[0] < n-1:
            result[0] +=1
print(str(result[0]+1)+' '+str(result[1]+1))