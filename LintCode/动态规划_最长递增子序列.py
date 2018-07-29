#dp方法求解最长递增子序列问题
# num=list(map(int,input().split(',')))
# dp=[1 for x in range(0,len(num))]
# maxdp=1
# for i in range(1,len(num)):
#     for j in range(0,i):
#         if num[i]>num[j] and dp[i]<dp[j]+1:#dp[i]<dp[j]+1保证i之前的序列有序
#             dp[i]=dp[j]+1
# print(max(dp))


num=list(map(int,input().split(',')))
dp=[1 for x in range(0,len(num))]

for i in range(0,len(num)):
    for j in range(0,i):
        if num[i]>num[j] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1
print(max(dp))
