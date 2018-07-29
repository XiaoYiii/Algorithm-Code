# 题目
# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含质因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

# 思路
# 每一个丑数必然是由之前的某个丑数与2，3或5的乘积得到的，
# 这样下一个丑数就用之前的丑数分别乘以2，3，5，找出这三这种最小的并且大于当前最大丑数的值，即为下一个要求的丑数。

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
    #     if index<=0:
    #         return 0
    #     if index==1:
    #         return 1
    #     flag,num,uglynum=True,1,1
    #     while flag:
    #         num=num+1
    #         numans=[]
    #         self.factor(num,numans)
    #         numans.sort()
    #         numans.reverse()
    #         if numans[0]<=5 and 4 not in numans and 1 not in numans:
    #             uglynum=uglynum+1
    #         if uglynum==index:
    #             return num
    #
    # def factor(self,n,factorans):
    #     n = int(n)
    #     for i in range(2, n//2+1):
    #         if n % i == 0:
    #             factorans.append(i)
    #             return self.factor(n//i,factorans)
    #     factorans.append(n)

        if (index <= 0):
            return 0
        uglyList = [1]
        indexTwo = 0
        indexThree = 0
        indexFive = 0
        for i in range(index-1):
            newUgly = min(uglyList[indexTwo]*2, uglyList[indexThree]*3, uglyList[indexFive]*5)
            uglyList.append(newUgly)
            if (newUgly % 2 == 0):
                indexTwo += 1
            if (newUgly % 3 == 0):
                indexThree += 1
            if (newUgly % 5 == 0):
                indexFive += 1
        return uglyList[-1]

if __name__=='__main__':
    solution=Solution()
    index=200
    ans=solution.GetUglyNumber_Solution(index)
    print(ans)


