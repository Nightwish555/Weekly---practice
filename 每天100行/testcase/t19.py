__author__="Nightwish"
__title__="interface"


#给定一个整数数组 nums 和一个目标值 target，
#请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#给定 nums = [2, 7, 11, 15], target = 13

def _test01(target):
    num1=[0,1,2,3]
    num=[2,7,11,15]
    nums=dict(zip(num1,num))
    for k,v in nums.items():
        for j in range(k+1,len(num)):
            if nums[k]+nums[j]==target:
                return (k,j)

#test_02()
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 子串:串中任意个连续的字符组成的子序列称为该串的子串

def _test02(s):
    res=0
    i=0
    for j in range(len(s)):
        if s[j] not in s[i:j]:
            res=max(res,j+1-i)
        else:
            i+=s[i:j].index(s[j])+1

#给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
def _test03(s):

    n=len(s)
    for i in range(len(s)):
        start=0
        end=n-i
        while end<=n:
            des_str=s[start:end]
            if _stringIs_equal(des_str):
                return des_str
            start+=1
            end+=1

def _stringIs_equal(s):
    return s==s[::-1]

print(_test03("ababs"))

#二分查找

def _test04(str:str,s):
    n=len(str)
    start=0
    end=n-1
    while start<=end:
        middle=(start+end)/2
        if s<s[middle]:
            end=middle-1
        if s>s[middle]:
            start=middle+1
        else:
            return middle
    return False

    def binary_search(lis, left, right, num):

        if left > right: #递归结束条件
            return -1
        mid = (left + right) // 2
        if num < lis[mid]:
            right = mid -1
        elif num > lis[mid]:
            left = mid + 1
        else:
            return mid
        return binary_search(lis, left, right, num)
        #这里之所以会有return是因为必须要接收值，不然返回None
        #回溯到最后一层的时候，如果没有return，那么将会返回None






