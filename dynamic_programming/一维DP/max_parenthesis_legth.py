# 给定一个括号字符串，求最长有效括号子串的长度。


def max_parenthesis_legth(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    dp = [0] * n
    pre = 0
    for i in range(1, n):
        if s[i] == ')':
            pre = i - dp[i-1] - 1
            if pre >= 0 and s[pre] == '(':
                dp[i] = dp[i-1] + 2 + (dp[pre-1] if pre > 0 else 0)
    
    return max(dp)


if __name__ == '__main__':
    s = "(()())"
    print(max_parenthesis_legth(s))
    
    s = "()(()"
    print(max_parenthesis_legth(s))
    
    s = "()()()"
    print(max_parenthesis_legth(s))
    
    s = "(()"
    print(max_parenthesis_legth(s))
    
    s = "()(()())"
    print(max_parenthesis_legth(s))