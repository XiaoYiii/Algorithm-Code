
item = list(map(int, input().split()))
n,k=item[0],item[1]
num=list(map(int,input().split()))
num=set(num)
num=sorted(num)
len=len(num)
ans=0
for i in range(0,len):
    for j in range(i,len):
        if j-i>k:
            break
        if num[j]-num[i]>k:
            break
        if num[j]-num[i]==k:
            ans+=1

print(ans)

# 5 2
# 1 5 3 4 2