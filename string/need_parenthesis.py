
# 括号匹配问题
# 给定一个只包含 '(' 和 ')' 的字符串，求最少需要添加多少个括号才能使得括号匹配。

def need_parenthesis(s):
    count = 0
    ans = 0 
    for i in s:
        if i == '(':
            count += 1
        else:
            if count == 0:
                ans += 1
            else:
                count -= 1
    return ans + count


if __name__ == '__main__':
    s = "(()))))"
    print(need_parenthesis(s))