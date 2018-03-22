


# problem 1

def cal(a,b):
    alen=len(a)
    blen=len(b)
    ans=0
    for i in range(0,alen-blen+1):
        temp=a[i:i+blen]
        for j in range(0,blen):
            if temp[j]!=b[j]:
                ans+=1
    return ans

if __name__=='__main__':
    a=input()
    b=input()
    ans=cal(a,b)
    print(ans)

# dp=[0 for i in range(0,len(b))]
# for p in range(len(temp)):
#     for q in range(len(b)):
#         if temp[p] == b[q]:
#             dp[p + 1][q + 1] = dp[p][q] + 1
#         else:
#             dp[p + 1][q + 1] = max(dp[p + 1][q], dp[p][q + 1])