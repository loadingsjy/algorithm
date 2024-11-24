# 官方题解
class Bitset:

    def __init__(self, size: int):
        self.arr = [0] * size  # 存储每一位的数组
        self.cnt = 0  # 1 的个数
        self.reversed = 0  # 反转操作的次数奇偶性

    def fix(self, idx: int) -> None:
        if self.arr[idx] ^ self.reversed == 0:
            self.arr[idx] ^= 1
            self.cnt += 1

    def unfix(self, idx: int) -> None:
        if self.arr[idx] ^ self.reversed == 1:
            self.arr[idx] ^= 1
            self.cnt -= 1

    def flip(self) -> None:
        self.reversed ^= 1
        self.cnt = len(self.arr) - self.cnt

    def all(self) -> bool:
        return self.cnt == len(self.arr)

    def one(self) -> bool:
        return self.cnt > 0

    def count(self) -> int:
        return self.cnt

    def toString(self) -> str:
        res = ""
        for bit in self.arr:
            res += str(bit ^ self.reversed)
        return res
