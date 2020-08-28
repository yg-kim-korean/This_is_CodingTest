#구현
n = input()
string = ''
temp = 0
for i in n:
    if i.isnumeric() == True:
        temp +=int(i)
    else:
        string+=i

result = sorted(string) 
result = ''.join(result) + str(temp)
print(result)
