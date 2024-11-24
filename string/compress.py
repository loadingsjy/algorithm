#
# * 443. 压缩字符串 - M

# 给你一个字符数组 chars ，请使用下述算法压缩：
# 从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：
# 如果这一组长度为 1 ，则将字符追加到 s 中。
# 否则，需要向 s 追加字符，后跟这一组的长度。
# 压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。
# 请在 修改完输入数组后 ，返回该数组的新长度。
# 你必须设计并实现一个只使用常量额外空间的算法来解决此问题。

# 示例 1：
# 输入：chars = ["a","a","b","b","c","c","c"]
# 输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
# 解释："aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
# 示例 2：
# 输入：chars = ["a"]
# 输出：返回 1 ，输入数组的前 1 个字符应该是：["a"]
# 解释：唯一的组是“a”，它保持未压缩，因为它是一个字符。
# 示例 3：
# 输入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# 输出：返回 4 ，输入数组的前 4 个字符应该是：["a","b","1","2"]。
# 解释：由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。

# 提示：
# 1 <= chars.length <= 2000
# chars[i] 可以是小写英文字母、大写英文字母、数字或符号


class Solution:
    def compress(self, chars: list[str]) -> int:
        """双指针法"""
        n = len(chars)
        i, j = 0, 0
        length = 1
        while i < n and j < n:
            while j + 1 < n and chars[j + 1] == chars[j]:
                length += 1
                j += 1
            chars[i] = chars[j]
            i += 1
            if length != 1:
                length = str(length)
                for k in range(len(length)):
                    chars[i] = length[k]
                    i += 1
            length = 1
            j += 1
        return i

    def compress(self, chars: list[str]) -> int:
        """两个指针 slow 和 fast ，其中快指针用于不断前进直到停止在不重复的字符，慢指针则停在重复字符的起点，
        因此 fast-slow 就是重复区间的长度。
        另设立一个 writer ，不断从头开始覆写 chars 数组"""
        slow = 0
        fast = 0
        writer = 0

        while fast < len(chars):
            while (
                fast < len(chars) and chars[fast] == chars[slow]
            ):  # fast不断前进，直到到达不重复的位置
                fast += 1

            distance = fast - slow  # 此时二者的差就是重复区间长度
            chars[writer] = chars[slow]  # 覆写一下字母，比如a, b
            writer += 1  # 写完后前进一步来准备写下个内容
            if distance > 1:
                dist_str = str(distance)

                # writer
                for i in range(len(dist_str)):
                    chars[writer] = dist_str[i]  # 开始写长度
                    writer += 1

            slow = fast  # 慢指针初始化为下一个char序列的起点，以准备计算新长度distance

        chars = chars[:writer]  # 截断结果
        return writer
