# 题目
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

# 示例
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap,ans={},[]
        for i in range(0,len(nums)):
            hashmap[nums[i]]=i
        for i in range(0,len(nums)):
            if hashmap.__contains__(target-nums[i]) and hashmap[target-nums[i]]!=i:
                ans.append(i)
                ans.append(hashmap[target-nums[i]])
                break
        return ans

solution=Solution()
nums=[3,2,4]
target=6
ans=solution.twoSum(nums,target)
print(ans)
