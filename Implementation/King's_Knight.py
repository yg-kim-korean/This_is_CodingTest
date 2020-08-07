n = input('시작위치 입력 : ')
xl = ['a','b','c','d','e','f','g','h']
x = int(n[1])
y = xl.index(n[0])+1
count = 0
steps = [(-2,1),(-2,-1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(1,-2)]

for i in steps:
    next_row = x+i[0]
    next_column = y+i[1]
    if next_row>=1 and next_row<=8 and next_column>=1 and next_row<=8:
        count+=1
print(count)





