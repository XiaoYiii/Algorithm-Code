class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        tempsum,maxsum=nums[0],nums[0]
        for i in range(1,len(nums)):
            if tempsum<0:
                tempsum=nums[i]
            else:
                tempsum=tempsum+nums[i]
            if tempsum>maxsum:
                maxsum=tempsum
        return maxsum

if __name__=='__main__':
    nums=list(map(int,input().split(',')))
    solution=Solution()
    ans=solution.maxSubArray(nums)
    print(ans)

