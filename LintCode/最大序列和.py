

def max_sum(num):
    sum,maxsum=0,0
    for i in range(0,len(num)):
        sum+=num[i]
        if sum>maxsum:
            maxsum=sum
        if sum<0:
            sum=0
    return maxsum

if __name__=='__main__':
    num=list(map(int,input().split(' ')))
    ans=max_sum(num)
    print(ans)