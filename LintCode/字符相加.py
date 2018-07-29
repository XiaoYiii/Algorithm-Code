# 计算过程只涉及到加减乘
# 输入
# 2
# 1+2
# 3-2
# 5*6
# 输出
# 66666
# ....6
# 66666
# ....6
# 66666
# 66666
# ....6
# 66666
# 6....
# 66666
# 66666.66666
# ....6.6...6
# 66666.6...6
# ....6.6...6
# 66666.66666


n=int(input())
num=[]
nn=['0' for i in range(10)]
nn[0]='66666\n6...6\n6...6\n6...6\n66666'
nn[1]='....6\n....6\n....6\n....6\n....6'
nn[2]='66666\n....6\n66666\n6....\n66666'
nn[3]='66666\n....6\n66666\n....6\n66666'
nn[4]='6...6\n6...6\n66666\n....6\n....6'
nn[5]='66666\n6....\n66666\n....6\n66666'
nn[6]='66666\n6....\n66666\n6...6\n66666'
nn[7]='66666\n....6\n....6\n....6\n....6'
nn[8]='66666\n6...6\n66666\n6...6\n66666'
nn[9]='66666\n6...6\n66666\n....6\n66666'
ans=['0' for i in range(n)]
for i in range(0,n):
    num = input()
    templen=len(num)
    tempans=0
    for j in range(0,templen):
        if num[j]=='+':
            a=int(num[0:j])
            b=int(num[j+1:templen])
            tempans=a+b
            break
        if num[j]=='-':
            a = int(num[0:j])
            b = int(num[j + 1:templen])
            tempans = a - b
            break
        if num[j]=='*':
            a = int(num[0:j])
            b = int(num[j + 1:templen])
            tempans = a * b
            break
    tempans=str(tempans)
    ans[i]=tempans

for i in range(n):
    tempans=ans[i]
    templen=len(ans[i])
    nowans=['' for i in range(0,5)]
    for k in range(0,5):
        for l in range(0,len(tempans)-1):
            if k==0:
                nowans[0]+=nn[int(tempans[l])][0:5]+'.'
            if k==1:
                nowans[1]+=nn[int(tempans[l])][6:11]+'.'
            if k==2:
                nowans[2]+=nn[int(tempans[l])][12:17]+'.'
            if k==3:
                nowans[3]+=nn[int(tempans[l])][18:23]+'.'
            if k==4:
                nowans[4]+=nn[int(tempans[l])][24:29]+'.'
        if k == 0:
            nowans[0] += nn[int(tempans[templen-1])][0:5]
        if k == 1:
            nowans[1] += nn[int(tempans[templen-1])][6:11]
        if k == 2:
            nowans[2] += nn[int(tempans[templen-1])][12:17]
        if k == 3:
            nowans[3] += nn[int(tempans[templen-1])][18:23]
        if k == 4:
            nowans[4] += nn[int(tempans[templen-1])][24:29]
        print(nowans[k])