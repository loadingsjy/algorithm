import sys


class UF:
    """并查集数组实现"""

    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i):
        """寻找i元素的根节点，并进行扁平化处理"""
        stack = []
        while i != self.father[i]:
            stack.append(i)
            i = self.father[i]
        while stack:
            self.father[stack.pop()] = i
        return i

    def isSameSet(self, x, y):
        """判断x和y是否在同一集合内"""
        return self.find(x) == self.find(y)

    def union(self, x, y):
        """合并x所在集合与y所在的集合(小挂大)"""
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            if self.size[fx] >= self.size[fy]:
                self.size[fx] += self.size[fy]
                self.father[fy] = fx
            else:
                self.size[fy] += self.size[fx]
                self.father[fx] = fy


if __name__ == "__main__":
    n, m = input().split()
    n, m = int(n), int(m)
    uf = UF(n)
    for line in sys.stdin:
        if line:
            opt, x, y = line.split()
            if opt == "1":
                if uf.isSameSet(int(x), int(y)):
                    print("Yes")
                else:
                    print("No")
            elif opt == "2":
                uf.union(int(x), int(y))
