# import numpy
#
# #最长子序列和问题
#
# def sum(len,num):
#
#
#
# if __name__=='__main__':
#     len = int(input())
#     num = [x for x in range(0, len)]
#     for i in range(0,len):
#         num[i]=
#     sum(len,sum)
def fib1(n):
    a,b=0,1
    while a<n:
        print(a,end='')
        a,b=b,a+b
        print()

def fib2(n):
    result=[]#this is a list
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result

print(fib2(1000))#print the list

def ask_ok(prompt,retries=4,reminder='Please try again!'):
    while True:
        ok=input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries=retries-1
        while retries<0:
            raise ValueError('invalid user response')
        print(reminder)
#The function can be called by few away!
#ask_ok('Do you really want to quit?')
#ask_ok('OK to overwrite the file?', 2)
#ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

def concat(*args,sep='/'):
    return sep.join(args)

print(concat('earth','mars','venus'))

args=[3,6]
list(range(*args))#*must be the list **must be the map

def make_incrementor(n):
    return lambda x:x+n

f=make_incrementor(42)
print(f(0))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]#map
pairs.sort(key=lambda pairs:pairs[1])
print(pairs)#按照第二个元素进行排序

a=[1,2,3,4,5]
import numpy
np=numpy.array
print(dir(numpy))
print(dir(np))

s='HelloWorld'
print(str(s))
print(repr(s))
print(1/7)
print(str(1/7))
print(repr(1/7))#repr将任意类型字符转换为字符串















