
# 1.汽水瓶
# 某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）。
# 小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。
# 数据范围：输入的正整数满足 1≤n≤100

# 注意：本题存在多组输入。输入的 0 表示输入结束，并不用输出结果。

# 输入文件最多包含 10 组测试数据，每个数据占一行，仅包含一个正整数 n（ 1<=n<=100 ），表示小张手上的空汽水瓶数。n=0 表示输入结束，你的程序不应当处理这一行。
# 对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。
import sys
def max_drinks(n):
    drinks = 0
    while n >= 3:
        huan = n // 3       # 每3个空瓶换一瓶
        drinks += huan
        rest = n % 3        # 剩余的空瓶数
        n = huan + rest     # 更新空瓶数，继续换瓶
    if n == 2:
        drinks += 1
    
    return drinks
    
    
if __name__ == '__main__':
    questions =[]
    for line in sys.stdin:
        a = int(line.strip())
        if a == 0:
            break
        questions.append(a)
    for q in questions:
        sys.stdout.write(str(max_drinks(q)) + '\n')