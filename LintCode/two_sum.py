#在一个序列中判断能否两个数相加得到target数据
#for example：[1,2,3,4,5] target=4
#return [0,2]

#直接思路是利用两个数进行相加，但是复杂度o(n*n)太高
#另外思路便是利用两个指针，头尾相加

def two_sum(target,nums=[]):
    nums_sort=nums
    nums_sort.sort()
    start,end=0,len(nums_sort)-1
    ans=[]
    while True:
        if nums_sort[start]+nums_sort[end]==target:
            for i in range(0,len(nums)):
                if nums[i]==nums_sort[start]:
                    ans.append(i)
            for j in range(0,len(nums)):
                if nums[j]==nums_sort[end]:
                    ans.append(j)
            return ans
        if nums_sort[start]+nums_sort[end]>target:
            end=end-1
        if nums_sort[start]+nums_sort[end]<target:
            start=start+1

if __name__=='__main__':
    nums=list(map(int,input().split()))
    target=int(input())
    print(two_sum(target,nums))