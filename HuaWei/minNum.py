# 题目描述
# 给一个数组，数组里面都是代表非负整数的字符串，将数组里所有的数值排列组合Q拼接起来组成一个数字， 输出拼成的最小的数
# 输入描述
# -个数组，数组不为空，数组里面都是代表非负整数的字符串，可以是0开头，例如:"13"， "045","09", "56"].
# 数组的大小范围: [1,50]
# 数组中每个元素的长度范围: [1,30]
# 输出描述:
# 以字符串的格式输出一个数字，如果最终结果是多位数字，要优先选择输出不是“0"开头的最小数字:如果拼接出的数字都是"0"开
# 头，则选取值最小的，并且把开头部分的“0”都去掉再输出;如果是单位数“0”，可以直接输出“0”
# 示例1
# 输入:
# 20 1
# 输出:
# 120
# 示例2
# 输入:
# 08 10 2
# 输出:
# 10082


from functools import cmp_to_key



def cmp(str1,str2):
    s1 = ''.join((str1,str2))
    s2 = ''.join((str2,str1))
    if s1 < s2:
        return -1
    elif s1 == s2:
        return 0
    else:
        return 1
    

def minNum(nums_str):
    '''贪心'''
    sorted_nums = sorted(nums_str, key=cmp_to_key(cmp))
    print(sorted_nums)
    
    for i, n_str in enumerate(sorted_nums):
        if n_str[0] != '0':
            sorted_nums[0], sorted_nums[i] = sorted_nums[i], sorted_nums[0]
            break
    res = ''.join(sorted_nums)
    return res.lstrip('0')      # 去掉左边的‘0’
            



if __name__ == "__main__":
    nums = ['08', '10', '2','23', '43', '6']
    print(minNum(nums))
    
    nums = ['08', '00', '02', '06']
    print(minNum(nums))