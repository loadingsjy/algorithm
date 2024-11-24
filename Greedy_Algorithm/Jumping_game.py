
# 能否跳到最后一块石头
# 给定一个非负整数数组，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一块石头。
# 示例 1:
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一块石头。
# 示例 2:
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的石头，但该石头的最大跳跃长度是 0 ， 所以你永远不可能到达最后一块石头。、

# 解题思路：
# 贪心算法，从左往右遍历数组，维护一个变量 max_reach，表示到当前位置的最大跳跃距离。
# 如果当前位置的跳跃距离大于 max_reach，说明无法到达最后一块石头，返回 False。
# 否则，更新 max_reach 为 max(max_reach, i + nums[i])，表示到达当前位置的最大跳跃距离。
# 遍历完成后，如果 max_reach 超过数组长度，说明可以到达最后一块石头，返回 True。


def canJump(nums):
    n = len(nums)
    cover = 0
    for i in range(n):
        if i > cover:
            return False
        cover = max(cover, i + nums[i])
    return True



# 最少跳跃次数
# 给定一个非负整数数组，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# 示例:
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。跳 1 步到达数组的位置 1，然后跳 3 步到达数组的最后一个位置。
# 说明:
# 假设你总是可以到达数组的最后一个位置。

def minium_jump(nums):
    n = len(nums)
    cur_cover = 0       # 当前位置的最大跳跃距离
    next_cover = 0      # 下一个位置的最大跳跃距离
    step = 0
    for i in range(n):
        next_cover = max(next_cover, i + nums[i])
        if i == cur_cover:       # 到达当前位置最后覆盖的位置
            if cur_cover < n-1:
                step += 1
                cur_cover = next_cover
                if cur_cover >= n-1:
                    break
            else:
                break
    return step
    


if __name__ == '__main__':
    nums = [2,3,1,1,4]
    print(canJump(nums))
    print(minium_jump(nums))    