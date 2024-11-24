

# 给定一个只由0(假)、1(真)、&(逻辑与)、|(逻辑或)、^(逻辑异或)五种字符组成的字符串expression，
# 以及一个布尔值desired，求expression中所有括号子表达式的结果等于desired的方法数。
# 注意：括号子表达式指的是由括号包围的子表达式。
# 例如，expression="1^0|1&0"，desired=True，则有2种方法：(1^((0|1)&0))、(((1^0)|1)&0)


# 判断表达式是否合法
def isValid(expression):
    if len(expression) & 1 == 0:    # 长度必须是奇数
        return False
    for i in range(0,len(expression),2):
        if expression[i] not in ['0','1']:
            return False
    for i in range(1,len(expression),2):
        if expression[i] not in ['&','|','^']:
            return False
    return True
    
    
def count_desired(expression, desired):
    if not expression:
        return False
    if not isValid(expression):
        return False
    return p(expression, desired, 0, len(expression)-1)



# expression: 表达式字符串，固定参数
# desired: 期望的结果,true/false
# left: 左边界
# right: 右边界，注意：left和right不能压中逻辑运算符！
# 返回left和right之间的表达式的结果等于desired的方法数
def p(expression, desired, left, right):
    if left == right:
        if expression[left] == '1':
            return 1 if desired else 0
        elif expression[left] == '0':
            return 1 if not desired else 0

    res = 0
    if desired:
        for i in range(left+1, right, 2):
            exp = expression[i]
            if exp == '&':
                # 左边为真的方法数乘上右边为真的方法数
                res += p(expression, True, left, i-1) * p(expression, True, i+1, right)
            elif exp == '|':
                res += p(expression, True, left, i-1) * p(expression, False, i+1, right)
                res += p(expression, False, left, i-1) * p(expression, True, i+1, right)
                res += p(expression, True, left, i-1) * p(expression, True, i+1, right)
            elif exp == '^':
                res += p(expression, True, left, i-1) * p(expression, False, i+1, right)
                res += p(expression, False, left, i-1) * p(expression, True, i+1, right)
    else:
        for i in range(left+1, right, 2):
            exp = expression[i]
            if exp == '&':
                res += p(expression, False, left, i-1) * p(expression, False, i+1, right)
                res += p(expression, False, left, i-1) * p(expression, True, i+1, right)
                res += p(expression, True, left, i-1) * p(expression, False, i+1, right)
            elif exp == '|':
                res += p(expression, False, left, i-1) * p(expression, False, i+1, right)
            elif exp == '^':
                res += p(expression, True, left, i-1) * p(expression, True, i+1, right)
                res += p(expression, False, left, i-1) * p(expression, False, i+1, right)
    return res


# 根据暴力递归该动态规划
def count_desired_dp(expression, desired):
    n = len(expression)
    dp_f = [[0] * n for _ in range(n)]
    dp_t = [[0] * n for _ in range(n)]
    for i in range(n):
        if expression[i] == '1':
            dp_f[i][i] = 0
            dp_t[i][i] = 1
        elif expression[i] == '0':
            dp_f[i][i] = 1
            dp_t[i][i] = 0
            
    for row in range(n - 3, -1, -2):
        for col in range(row + 2, n, 2):
            for i in range(row + 1, col, 2):
                exp = expression[i]
                if exp == '&':
                    dp_f[row][col] += dp_f[row][i-1] * dp_f[i+1][col] + dp_t[row][i-1] * dp_f[i+1][col] + dp_f[row][i-1] * dp_t[i+1][col]
                    dp_t[row][col] += dp_t[row][i-1] * dp_t[i+1][col]
                elif exp == '|':
                    dp_f[row][col] += dp_f[row][i-1] * dp_f[i+1][col]
                    dp_t[row][col] += dp_t[row][i-1] * dp_t[i+1][col] + dp_t[row][i-1] * dp_f[i+1][col] + dp_f[row][i-1] * dp_t[i+1][col]
                elif exp == '^':
                    dp_f[row][col] += dp_f[row][i-1] * dp_f[i+1][col] + dp_t[row][i-1] * dp_t[i+1][col]
                    dp_t[row][col] += dp_t[row][i-1] * dp_f[i+1][col] + dp_f[row][i-1] * dp_t[i+1][col]
            

    return dp_t[0][n-1] if desired else dp_f[0][n-1]


if __name__ == '__main__':
    expression = "1^0|1&0"
    desired = True
    print(count_desired(expression, desired))
    print(count_desired_dp(expression, desired))
    print()
    
    expression = "1^0|1&0"
    desired = False
    print(count_desired(expression, desired))
    print(count_desired_dp(expression, desired))
    print()
    
    expression = "0&0&0&1^1|0|1"
    desired = True
    print(count_desired(expression, desired))
    print(count_desired_dp(expression, desired))
    
    