# 简单位图实现


class Bitset(object):
    def __init__(self, n):
        """初始化位图，数组中每个数字的32二进制位表示该数存在或不存在"""
        # a/b的结果 如果响向上取整，可以写成：（a+b-1)//b
        self.bitset = [0] * ((n + 31) // 32)

    def add(self, num):
        """增加一个数字"""
        self.bitset[num // 32] |= 1 << (num % 32)

    def remove(self, num):
        """删除当前数字，如果不存在，则不删"""
        self.bitset[num // 32] &= ~(1 << num % 32)

    def contains(self, num):
        """是否包含当前数字"""
        return ((self.bitset[num // 32] >> (num % 32)) & 1) == 1

    def reverse(self, num):
        """反转当前数字"""
        self.bitset[num // 32] ^= 1 << (num % 32)


if __name__ == "__main__":
    b = Bitset(36)
    b.add(1)
    b.add(2)
    b.add(3)
    b.add(4)
    b.add(5)
    b.remove(4)
    print(b.contains(3))
    print(b.contains(4))
