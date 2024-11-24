# 列表 arr 由在范围 [1, n] 中的所有整数组成，并按严格递增排序。请你对 arr 应用下述算法：
# 从左到右，删除第一个数字，然后每隔一个数字删除一个，直到到达列表末尾。
# 重复上面的步骤，但这次是从右到左。也就是，删除最右侧的数字，然后剩下的数字每隔一个删除一个。
# 不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
# 给你整数 n ，返回 arr 最后剩下的数字。


# 示例 1：
# 输入：n = 9
# 输出：6
# 解释：
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [2, 4, 6, 8]
# arr = [2, 6]
# arr = [6]
# 示例 2：
# 输入：n = 1
# 输出：1


class Solution:
    def lastRemaining(self, n: int) -> int:
        a1 = 1  # 当前第一个元素的值
        k, cnt, step = 0, n, 1  # k：正向、反向；cnt:数组当前的长度；step：当前移动步长
        while cnt > 1:
            if k % 2 == 0:  # 正向
                a1 += step
            else:  # 反向
                if cnt % 2:
                    a1 += step
            k += 1
            cnt >>= 1
            step <<= 1
        return a1

    def lastRemaining2(self, n: int) -> int:
        '''错误'''
        a1 = 1  # 当前第一个元素的值
        k = 0  # 偶数正向、奇数反向
        cur_len = n  # 数组当前的长度
        step = 2  # 当前移动步长

        while cur_len > 1:
            while 1 <= a1 <= n:
                if k % 2 == 0:
                    a1 += step
                else:
                    a1 -= step

            if k % 2 == 0:
                if cur_len & 1 == 1:  # 当前长度为奇数
                    a1 -= 1
                else:
                    a1 += 1
            else: 
                if cur_len & 1 == 1:  # 当前长度为奇数
                    a1 += 1
                else:
                    a1 -= 1
            
            k += 1
            step *= 2
            cur_len //= 2

        return a1


if __name__ == "__main__":
    s = Solution()
    n = 9
    print(s.lastRemaining(n))
    print(s.lastRemaining2(n))
