def quick_sort(num,left,right):
    if left>=right:
        return num
    key,low,high=num[left],left,right#key是标准数
    while left<right:
        while left<right and num[right]>=key:
            right-=1
        num[left]=num[right]
        while left<right and num[left]<=key:
            left+=1
        num[right]=num[left]
    num[right]=key
    quick_sort(num,low,left-1)
    quick_sort(num,right+1,high)
    return num

num=list(map(int,input().split()))
len=len(num)
k=num[len-1]
del num[len-1]
len=len-1
num=quick_sort(num,0,len-1)
flag=True
for i in range(0,k):
    if flag==True:
        print(num[i],end='')
        flag=False
    else:
        print('',num[i],end='')