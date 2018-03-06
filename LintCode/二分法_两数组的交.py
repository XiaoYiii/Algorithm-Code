#返回两个数组的交集


class Solution:
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """

    # def intersection(self, nums1, nums2):
    # # write your code here
    #     nums1=list(set(nums1))
    #     nums2=list(set(nums2))
    #     ans=[]
    #     for i in range(0,len(nums2)):
    #         if nums2[i]  in nums1:
    #             ans.append(nums2[i])
    #     return ans

    def findNum(self, n, num=[]):
        low, high = 0, len(num) - 1
        while low <= high:
            mid = (low + high) // 2
            if num[mid] == n:
                return True
            if num[mid] > n:
                high -= 1
            if num[mid] < n:
                low += 1
        return False

    def intersection(self,nums1,nums2):
        # write your code in here
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        nums2.sort()
        ans=[]
        for i in range(0,len(nums1)):
            temp=self.findNum(nums1[i],nums2)
            if temp==True:
                ans.append(nums1[i])
            else:
                pass
        return ans

if __name__=="__main__":
    solution=Solution()
    nums1=list(map(int,input().split(' ')))
    nums2=list(map(int,input().split(' ')))
    ans=solution.intersection(nums1,nums2)
    print(ans)