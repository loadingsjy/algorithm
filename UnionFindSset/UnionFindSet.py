class element:
    """元素类"""

    def __init__(self, value=0):
        self.value = value


class UnionFindSet:
    """并查集实现"""

    def __init__(self, lists):
        self.elememtsMap = dict()
        self.parentMap = dict()
        self.sizeMap = dict()

        for l in lists:
            ele_l = element(l)
            self.elememtsMap[l] = ele_l  # 元素与元素的映射
            self.parentMap[ele_l] = ele_l  # 初始时，每个元素的父节点都是自己
            self.sizeMap[ele_l] = 1  # 初始时，每个元素的大小都是1

    def findHead(self, element):
        """寻找元素的根节点"""
        stack = []
        while self.parentMap.get(element) != element:
            stack.append(element)
            element = self.parentMap[element]

        # 路径压缩，把当前节点的父节点指向根节点
        while stack:
            self.parentMap[stack.pop()] = element
        return element

    def isSameSet(self, l1, l2):
        """判断两个元素是否属于同一集合"""
        ele1 = self.elememtsMap.get(l1)
        ele2 = self.elememtsMap.get(l2)
        if ele1 is not None and ele2 is not None:
            return self.findHead(ele1) == self.findHead(ele2)
        return False

    def union(self, a, b):
        """合并两个集合"""
        if self.elememtsMap.get(a) is not None and self.elememtsMap.get(b) is not None:
            a_root = self.findHead(self.elememtsMap.get(a))
            b_root = self.findHead(self.elememtsMap.get(b))
            if a_root != b_root:
                if self.sizeMap[a_root] < self.sizeMap[b_root]:
                    a_root, b_root = b_root, a_root
                # 合并两个集合，a为元素多的集合，b为元素少的集合
                self.parentMap[b_root] = a_root
                self.sizeMap[a_root] += self.sizeMap[b_root]
                # 删除b_root节点
                del self.sizeMap[b_root]


if __name__ == "__main__":
    uf = UnionFindSet([1, 2, 3, 4, 5])
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(4, 5)
    # uf.union(3, 4)
    print(uf.isSameSet(1, 2))
    print(uf.isSameSet(2, 3))
    print(uf.isSameSet(4, 5))
    print(uf.isSameSet(3, 4))
