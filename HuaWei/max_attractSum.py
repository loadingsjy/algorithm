# 讨厌鬼的组合帖子
# 题目描述
# 讨厌鬼有 n 个帖子。第 i 个帖子的点赞数为 a[i] 点踩数为 b[i]。你可以选择任意个帖子组合起来。
# 组合帖子的点赞数和点踩数为所有被组合帖子点赞数和点踩数之和。已知一个帖子的点赞数为 x，点踩数为 y，则该帖子的吸引度为 |x - y|。
# 讨厌鬼需要选择若干个帖子组合起来，使得这个组合帖子的吸引度尽可能大。请你告诉他这个吸引度最大是多少？

# 输入描述
# 第一行输入一个整数 n(1 <= n <= 10^5)。
# 第二行输入 n 个整数 a[i](1 <= a[i] <= 10^9)
# 第三行输入 n 个整数 b[i](1 <= b[i] <= 10^9)。

# 输出描述
# 一行一个整数，表示最大吸引度。
# 输入示例
# 4
# 4 2 1 1
# 2 1 4 4

# 输出示例
# 6
# 提示信息
# 选择第 3 个和第 4 个帖子组合后，点赞数为 2，点踩数为 8，吸引度为|2 - 8| = 6。


def max_attractSum(a, b):
    attracts = [x - y for x, y in zip(a, b)]

    n = len(attracts)
    # dp_max = [0] * n
    # dp_min = [0] * n

    # dp_max[0] = max(attract[0], 0)
    # dp_min[0] = min(attract[0], 0)

    # for i in range(1, n):
    #     dp_max[i] = max(dp_max[i - 1] + attract[i], attract[i])
    #     dp_min[i] = min(dp_min[i - 1] + attract[i], attract[i])
    # return max(abs(max(dp_max)), abs(min(dp_min)))
    zheng_sum = 0
    fu_sum = 0
    for a in attracts:
        if a >= 0:
            zheng_sum += a
        else:
            fu_sum += a
    return max(zheng_sum, abs(fu_sum))
            
        


n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(max_attractSum(a, b))
