#
# * 1109. 航班预订统计

# 这里有 n 个航班，它们分别从 1 到 n 进行编号。
# 有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi]
# 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。
# 请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。


class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        cnt = [0] * (n + 2)  # 编号从1开始，最后一个是为了防止last超
        for frist, last, seat in bookings:
            cnt[frist] += seat
            cnt[last + 1] -= seat

        for i in range(1, n + 2):
            cnt[i] += cnt[i - 1]
        return cnt[1:-1]


if __name__ == "__main__":
    s = Solution()
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    print(s.corpFlightBookings(bookings, n))
