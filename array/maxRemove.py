# 给定一个由纯数字组成以字符串表示的数值， 现要求字符串中的每 个数字最多只能出现2次，超过的需要进行删除;
# 删除某个重复的数字后，其它数字相对位置保持不变。
# 如"34533",数字3重复超过2次，需要删除其中一个3,删除第一个3后获得最大数值”4533"
# 请返回经过删除操作后的最大的数值，以字符串表示。
# 输入描述
# 第一行为一个纯数字组成的字符串，长度范围: [1,100000]
# 输出描述
# 输出经过删除操作后的最大的数值
# 示例1
# 输入:
# 34533
# 输出:
# 4533
# 示例2
# 输入:
# 5445795045
# 输出:
# 5479504


from collections import Counter,defaultdict

# 一个长整型数字，消除重复的数字后，得到最大的一个数字。
def maxRemove_1(num_str):
    num_lst = list(num_str)
    cnt = Counter(num_lst)
    stack = list()          
    used = set()          
    for num in num_lst:
        if num in used:
            cnt[num] -= 1
        else:
            while stack and num > stack[-1] and cnt[stack[-1]] > 0:
                used.remove(stack[-1])  
                stack.pop()            
            stack.append(num)
            cnt[num]-=1
            used.add(num)
    return "".join(stack)


# 一个长整型数字，允许每个数字最多出现两次，消除重复的数字后，得到最大的一个数字。
def maxRemove_2(num_str):
    num_lst = list(num_str)
    cnt = Counter(num_lst)  # 剩余可用
    stack = list()          # 单调栈，栈底元素大，栈顶元素小
    used = defaultdict(int) # 已经使用
    for num in num_lst:
        if used[num] == 2:  # 已经使用过两次了
            cnt[num] -= 1
        else:
            # 当前数字大于栈顶数字，且栈顶数字出现超过两次，那么为了选出最大元素，需要剔除栈顶数字，放入当前数字
            while stack and num > stack[-1] and used[stack[-1]] + cnt[stack[-1]] > 2:
                used[stack[-1]] -= 1
                stack.pop()
            
            stack.append(num)
            cnt[num] -= 1
            used[num] += 1

    return "".join(stack)




if __name__ == '__main__':
    num_str = '34533'
    print(maxRemove_1(num_str))
    print(maxRemove_2(num_str))
    
    num_str = '5445795045'
    print(maxRemove_1(num_str))
    print(maxRemove_2(num_str))
