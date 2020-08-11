n = int(input('학생 수 : '))
array = []
for i in range(n):
    input_data = input(str(i+1)+'번째 학생과 점수 입력 : ').split()
    array.append((input_data[0],int(input_data[1])))

array.sort(key=lambda student: student[1])


for student in array:
    print(student[0],end = ' ')