#最大子序列和问题
num=list(map(int,input().split()))
n=len(num)
tempsum,max=0,0
for i in range(0,n):
    tempsum+=num[i]
    if tempsum>max:
        max=tempsum
    if tempsum<0:
        tempsum=0
print(max)

#sample -2  11 -4 13 -5 2 -5 -3 12 -9
#answer 21