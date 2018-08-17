# 题目
# 求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
# 为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
# ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
#
# 思路
# 对每个数字的每位进行分解，含有1则结果加一

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        ans=0
        for i in range(1,n+1):
            tempans=0
            while i!=0:
                eachnum=i%10
                i=i//10
                if eachnum==1:
                    tempans=tempans+1
            ans=ans+tempans
        return ans



if __name__=='__main__':
    n=130
    solution=Solution()
    ans=solution.NumberOf1Between1AndN_Solution(n)
    print(ans)