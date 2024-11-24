# 小红的第16版方案
# 题目描述：
# 小红正在做一个计划，她先写了份初版方案，但是领导不太满意，让小红改一改。
# 改着改着，小红就改了 16 版方案，然后领导说，还是用初版方案吧，现在小红非常的.....
# 小红组内有 n 个人，大家合作完成了一个初版方案，初始时大家的愤怒值都是 0。
# 但是领导对方案并不满意，共需要修改 m 次方案，每次修改会先让第 l 到 r 个人的愤怒值加 1，然后再修改方案。
# 组内每个人都有一个愤怒阈值 a，一旦第 i 次修改时有人愤怒值大于愤怒闻值，
# 他就会去找领导对线，直接将最终的方案定为第 i - 1 方案，并且接下来方案都不需要再修改了。
# 小红想知道，最终会使用第几版方案。初版方案被认为是第 0 版方案。

# 输入描述
# 第一行输入两个整数 n, m(1 <= n, m <= 10^5)表示数组长度和修改次数。
# 第二行输入 n 个整数表示数组a(0 <= a <= 10^9)
# 接下来 m 行，每行输入两个整数l, r(1 <= l <= r <= n)

# 输出描述
# 输出一个整数表示答案
# 输入示例
# 2 3
# 2 2
# 1 1
# 1 2
# 2 2
# 输出示例
# 3

# 提示信息
# 改为三次方案，大家的愤怒度都为 2，都不超过愤怒阈值，所以使用最后一版方案。


# 未通过
def plan(n, m, a, changes):
    angry = [0] * n
    # assert m == len(changes)
    i = 0
    flag = False
    while i < m:
        start, end = changes[i]     # 需要增加憤怒值的人的id[start, end]
        for index in range(start-1, end):
            angry[index] += 1
            if angry[index] > a[index]:
                flag = True
                break
        i += 1
        if flag:
            return i
    return i

n, m = input().split()
m = int(m)
n = int(n)

a = list(map(int, input().split()))

changes = []
for i in range(m):
    start, end = input().split()
    changes.append((int(start), int(end)))

print(plan(n, m, a, changes))
