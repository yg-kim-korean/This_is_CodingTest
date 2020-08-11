n,k = map(int,input('N K 입력 : ').split())
arr1 = list(map(int,input('첫번째 N 개 입력 : ').split()))
arr2 = list(map(int,input('두번째 N 개 입력 : ').split()))

# for _ in range(k):
#     temp1 = min(arr1)
#     temp2 = max(arr2)
#     itemp1 = arr1.index(temp1)
#     itemp2 = arr2.index(temp2)
#     arr1[itemp1],arr2[itemp2] = arr2[itemp2],arr1[itemp1]
arr1.sort()
arr2.sort(reverse=True)
for i in range(k):
    if arr1[i] < arr2[i]:
        arr1[i],arr2[i] = arr2[i],arr2[i]
    else:
        break
print(sum(arr1))