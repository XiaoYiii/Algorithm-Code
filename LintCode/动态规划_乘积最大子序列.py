#定个最大值和最小值

class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        #序列连续
        #找两个最值 保留每一步最大值和最小值
        maxnum,minnum,ans=nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            tempmax=maxnum*nums[i]
            tempmin=minnum*nums[i]
            maxnum=max(max(tempmax,tempmin),nums[i])#三者之中的最大值
            minnum=min(min(tempmax,tempmin),nums[i])#三者之中的最小值
            ans=max(ans,maxnum)
        return ans

    def maxProduce2(self,nums):
        #write you code here
        #序列不连续
        positive_num_list=[one for one in nums if one>1]
        negative_num_list=[one for one in nums if one<0]
        res1=res2=1
        if positive_num_list:
            res1=lambda x,y:x*y,positive_num_list
        if negative_num_list:
            if len(negative_num_list)%2!=0:
                negative_num_list.sort()
                negative_num_list=negative_num_list[:-1]
            res2=lambda x,y:x*y,negative_num_list
        return res1*res2

if __name__=='__main__':
    nums=list(map(int,input().split(' ')))
    solution=Solution()
    ans=solution.maxProduct(nums)
    print(ans)