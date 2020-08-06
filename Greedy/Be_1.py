n,k = map(int,input('N K 입력 : ').split())
count = 0
while True:
    
    if n%k == 0 :
        n//=k
    else:
        n=n-1


    count+=1
    if n==1:
        break
    

print(count)