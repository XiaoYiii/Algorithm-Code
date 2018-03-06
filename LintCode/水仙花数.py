num_flag=[0 for i in range(1000)]
for i in range(0,1000):
    num_flag[i]=0
for i in range(111,1000):
    a=int(i/100)
    b=int((i%100)/10)
    c=int(i%10)
    if a**3+b**3+c**3==i:
        num_flag[i]=1

flag = 'false'
t=1
m,n = map(int,input().split())
for i in range(m, n + 1):
    if num_flag[i] == 1:
        flag = 'true'
        if t==1:
            print(i, end='')
            t=0
        else:
            print('',i,end='')

if flag == 'false':
    print('no')