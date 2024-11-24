# 洛谷 P3367
# 题目描述：
# 如题，现在有一个并查集，你需要完成合并和查询操作。


import sys


class UF:
    """并查集  简单版实现"""

    def __init__(self, n):
        self.father = [i for i in range(n + 1)]

    def find(self, i):
        if i != self.father[i]:
            self.father[i] = self.find(self.father[i])
        return self.father[i]

    def isSameSet(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        self.father[self.find(x)] = self.find(y)


if __name__ == "__main__":
    n, m = input().split()
    n, m = int(n), int(m)
    uf = UF(n)
    for line in sys.stdin:
        if line:
            opt, x, y = line.split()
            if opt == "2":
                if uf.isSameSet(int(x), int(y)):
                    print("Y")
                else:
                    print("N")
            elif opt == "1":
                uf.union(int(x), int(y))
