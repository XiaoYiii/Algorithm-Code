# 题目
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for line in array:
            if target in line:
                return True
        return False

if __name__=='__main__':
    target=2
    array=[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]
    solution=Solution()
    ans=solution.Find(target,array)
    print(ans)