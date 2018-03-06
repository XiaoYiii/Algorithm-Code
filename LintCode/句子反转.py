str=list(map(str,input().split()))
len=len(str)
t=1
for i in range(len-1,-1,-1):
    if t==1:
        print(str[i],end='')
        t=0
    else:
        print('',str[i],end='')

