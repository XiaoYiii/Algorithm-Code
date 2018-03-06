#给出二维平面上的n个点，求最多有多少点在同一条直线上。

# 样例
# 给出4个点：(1, 2), (3, 6), (0, 0), (1, 3)。
#
# 一条直线上的点最多有3个。

#算法
#o(n*n)
#o(n*n)求出两者之间的概率
#然后找出概率相同的数，并找出最多相同的数据
#其中找出相同的数据利用hash 然后利用count统计出现的次数

#Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param: points: an array of point
    @return: An integer
    """

    def maxPoints(self, points):
        # write your code here
        if len(points)==0:
            return 0
        if len(points)==1:
            return 1
        maxnum=0
        for i in range(0,len(points)):
            templist=[]
            for j in range(0,len(points)):
                if i !=j:
                    if points[j].x-points[i].x==0:
                        templist.append(999999)
                    else:
                        templist.append((points[j].y-points[i].y)/(points[j].x-points[i].x))
            tempans = max(set(templist), key=templist.count)
            tempans=templist.count(tempans)
            if tempans > maxnum:
                maxnum = tempans
        return maxnum+1

if __name__=='__main__':
    #input the points
    n=int(input())
    points=[]
    for i in range(0,n):
        point=Point()
        temp=list(map(int,input().split(' ')))
        point.x,point.y=temp[0],temp[1]
        points.append(point)

    solution = Solution()
    ans=solution.maxPoints(points)
    print(ans)

