n = int(input('몇개 넣을래? : '))
array = []
for i in range(n):
    array.append(int(input(str(i+1)+'번째 숫자 : ')))

# for i in range(1,len(array)):
#     for j in range(i,0,-1):
#         if array[j] > array[j-1]:
#             array[j],array[j-1] = array[j-1],array[j]
array.sort(reverse=True)

for i in array:
    print(i , end = ' ')