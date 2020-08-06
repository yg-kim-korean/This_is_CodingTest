change = [500,100,50,10]
count = 0
money = int(input('잔돈을 입력하세요 : '))
for i in change:
    print(str(i)+'원 짜리는 '+str(money//i)+'개 입니다.')
    count += money//i
    money = money%i
    
print('총 필요한 동전 개수는 '+str(count)+'개 입니다.')