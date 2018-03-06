
# 给定一个数将其转换为二进制（均用字符串表示），如果这个数的小数部分不能在 32 个字符之内来精确地表示，则返回 "ERROR"。
# n = "3.72", 返回 "ERROR".
#
# n = "3.5", 返回 "11.1".


class Solution:
    """
    @param n: Given a decimal number that is passed in as a string
    @return: A string
    """
    def binaryRepresentation(self, n):
        # write your code here
        n=float(n)
        num1,num2=int(n),round(n-int(n),12)#3.5 3,0.5
        #处理整数部分
        num1list=[]
        while num1!=0:
            num1list.append(num1%2)
            num1//=2
        num1list.reverse()
        if len(num1list)==0:
            num1list.append(0)
        num1list=list(map(str,num1list))
        num1list = "".join(num1list)

        #处理小数部分
        num2list=[]
        while num2!=0:
            num2=num2*2
            num2list.append(int(num2))
            num2=num2-int(num2)
        # if len(num2list)>5:
        #     return "ERROR"
        num2list=list(map(str,num2list))
        num2list="".join(num2list)

        #ans
        ans=num1list
        if len(num2list)!=0:
            ans=num1list+'.'+num2list
        return ans


if __name__=='__main__':
    solution=Solution()
    n=input()
    ans=solution.binaryRepresentation(n)
    print(ans)