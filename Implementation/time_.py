n = int(input('정수 입력 : '))
time = [0,0,0]
count1 = 0
while int(time[0])<n+1:
    time[2] +=1
    if time[2] == 60:
        time[1] +=1
        time[2] = 0
        if time[1] ==60:
            time[0] +=1
            time[1] = 0
    x = (str(time[0]) + str(time[1]) +str(time[2]))
    if '3' in x :
        count1+=1
print(count1)
