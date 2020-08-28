#그리디
data = input()
count0 = 0
count1 = 0
#첫번째 원소 처리
if data[0] =='1':
    count0 +=1
else:
    count1 +=1

#두번째 원소부터 모든 원소를 확인하며
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        #다음수 에서 1로 바뀌는 수
        if data[i+1] =='1':
            count0 += 1
        else:
            count1 += 1
print(min(count0,count1))
    
    