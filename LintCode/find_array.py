import numpy as np
n = int(input())#表示学生个数
score = list(map(int,input().split()))#表示学生能力值 以后读取利用此类方式 先用map进行读取 然后转换为list 最后转换为数组形式
K,D = map(int,input().split())

fmax=[[0 for j in range(K)] for i in range(n)]
fmin=[[0 for j in range(K)] for i in range(n)]

res=0
for i in range (0,n):
    fmax[i][0]=fmin[i][0]=score[i]
    for k in range(1,min(i+1,K)):
        for j in range(max(0,i-D),i):
            fmax[i][k]=max(fmax[i][k],max(fmax[j][k-1]*score[i],fmin[j][k-1]*score[i]))
            fmin[i][k]=min(fmin[i][k],min(fmax[j][k-1]*score[i],fmin[j][k-1]*score[i]))

    res=max(res,fmax[i][K-1])
print(res)

