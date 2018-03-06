class Solution:
    """
    @param: num1: a non-negative integers
    @param: num2: a non-negative integers
    @return: return product of num1 and num2
    """
    def multiply(self, num1, num2):
        # write your code here
        num1=num1[::-1]
        num1=list(map(int,num1))
        num2=num2[::-1]
        num2=list(map(int,num2))
        if num1[0]==0 or num2[0]==0:
            return "0"
        ans=[0 for i in range(0,len(num1)+len(num2))]
        for i in range(0,len(num1)):
            for j in range(0,len(num2)):
                ans[i+j]+=num1[i]*num2[j]
        for k in range(0,len(ans)):
            if ans[k]>9:
                ans[k+1]+=ans[k]//10
                ans[k]=ans[k]%10
        ans=list(map(str,ans))
        ans="".join(ans)
        ans=ans[::-1]
        if ans[0]=='0':
            return ans[1:len(ans)]
        else:
            return ans

if __name__=='__main__':
    solution=Solution()
    num1=input()
    num2=input()
    ans=solution.multiply(num1,num2)
    print(ans)