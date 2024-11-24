#
# * 2166. 设计位集
# 位集 Bitset 是一种能以紧凑形式存储位的数据结构。

# 请你实现 Bitset 类。
# Bitset(int size) 用 size 个位初始化 Bitset ，所有位都是 0 。
# void fix(int idx) 将下标为 idx 的位上的值更新为 1 。如果值已经是 1 ，则不会发生任何改变。
# void unfix(int idx) 将下标为 idx 的位上的值更新为 0 。如果值已经是 0 ，则不会发生任何改变。
# void flip() 翻转 Bitset 中每一位上的值。换句话说，所有值为 0 的位将会变成 1 ，反之亦然。
# boolean all() 检查 Bitset 中 每一位 的值是否都是 1 。如果满足此条件，返回 true ；否则，返回 false 。
# boolean one() 检查 Bitset 中 是否 至少一位 的值是 1 。如果满足此条件，返回 true ；否则，返回 false 。
# int count() 返回 Bitset 中值为 1 的位的 总数 。
# String toString() 返回 Bitset 的当前组成情况。注意，在结果字符串中，第 i 个下标处的字符应该与 Bitset 中的第 i 位一致。


class Bitset:

    def __init__(self, size: int):
        """初始化位图，数组中每个数字的32二进制位表示该数存在或不存在"""
        # a/b的结果 如果响向上取整，可以写成：（a + b - 1) // b
        self.bitset = [0] * ((size + 31) // 32)
        self.size = size
        self.zeros = size
        self.ones = 0
        # 整个位图是否经历过翻转 :
        # reverse = False：1：代表存在，0：代表不存在；reverse = True：0：代表存在，1：代表不存在
        self.reverse = False

    def fix(self, idx: int) -> None:
        index = idx // 32
        bit = idx % 32
        if not self.reverse:
            # 位图所有的状态，维持原始含义： 0：不存在；1：存在
            if self.bitset[index] & (1 << bit) == 0:
                self.ones += 1
                self.zeros -= 1
                self.bitset[index] |= 1 << bit
        else:
            # 位图所有的状态翻转了： 1：不存在；0：存在
            if self.bitset[index] & (1 << bit) != 0:
                self.ones += 1
                self.zeros -= 1
                self.bitset[index] ^= 1 << bit

    def unfix(self, idx: int) -> None:
        index = idx // 32
        bit = idx % 32
        if not self.reverse:
            # 位图所有的状态，维持原始含义： 0：不存在；1：存在
            if self.bitset[index] & (1 << bit) != 0:
                self.ones -= 1
                self.zeros += 1
                self.bitset[index] ^= 1 << bit
        else:
            if self.bitset[index] & (1 << bit) == 0:
                self.ones -= 1
                self.zeros += 1
                self.bitset[index] |= 1 << bit

    def flip(self) -> None:
        self.reverse = not self.reverse
        self.ones, self.zeros = self.zeros, self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        string = []
        i = 0  # 0 ~ size
        k = 0  # 数组index：0 ~ (size//32 向上取整)
        while i < self.size:
            num = self.bitset[k]
            j = 0  # j：0 ~ 32
            while j < 32 and i < self.size:
                status = (num >> j) & 1
                status ^= 1 if self.reverse else 0
                string.append(status)
                i += 1
                j += 1
            k += 1
        return "".join(map(str, string))
