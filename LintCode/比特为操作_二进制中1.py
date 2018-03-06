# 计算在一个 32 位的整数的二进制表示中有多少个 1.
#
# 给定 32 (100000)，返回 1
#
# 给定 5 (101)，返回 2
#
# 给定 1023 (1111111111)，返回 10
class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        # write your code here
        ans=0
        if num==0:
            return 0
        if num<0:
            num+=pow(2,32)#当n为负数的时候为2的32次方再加上n值
        while num!=1:
            if num%2==1:
                ans+=1
            num//=2
        return ans+1

if __name__=='__main__':
    solution=Solution()
    num=int(input())
    ans=solution.countOnes(num)
    print(ans)