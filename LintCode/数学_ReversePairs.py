#description
# For an array A, if i < j, and A [i] > A [j], called (A [i], A [j]) is a reverse pair.
# return total of reverse pairs in A.

#for example
#Given A = [2, 4, 1, 3, 5] , (2, 1), (4, 1), (4, 3) are reverse pairs. return 3

#最简单采用O(n*n)的排序方法 但复杂度过高

# 归并排序
def merge_sort(ans,l=[]):
    # 对列表进行二分分解
    n = len(l)
    if n <= 1:
        return l
    mid_posi = n // 2  # //保留除后整数部分

    # 进行递归排序
    l_list = merge_sort(ans,l[:mid_posi])  # 采用递归的方式进行排序 递归左半序列
    r_list = merge_sort(ans,l[mid_posi:])  # 采用递归的方式进行排序 递归右半序列

    # 对列表进行合并
    sorted_list = []
    l_posi = 0
    r_posi = 0

    while l_posi < len(l_list) and r_posi < len(l_list):
        if l_list[l_posi] <= r_list[r_posi]:
            sorted_list.append(l_list[l_posi])
            l_posi += 1
        else:
            sorted_list.append(r_list[r_posi])
            r_posi += 1
            ans+=mid_posi-r_posi+1

    # 将列表剩余部分合并
    sorted_list += l_list[l_posi:]
    sorted_list += r_list[r_posi:]
    print(ans)
    return sorted_list

if __name__=='__main__':
    nums=list(map(int,input().split()))
    #ans=solve1(nums) #采用o(n*n)方法进行解决
    ans=0
    sorted_nums=merge_sort(ans,nums)#采用递归排序进行解决
    print(ans)