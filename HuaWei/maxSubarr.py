# 区块链底层存储是一个链式文件系统，由顺序的N个文件组成，每个文件的大小不一，依次为F1，F2...Fn。随着时间的推移，所占存储会越来越大。
# 云平台考虑将区块链按文件转储到廉价的SATA盘，只有连续的区块链文件才能转储到SATA盘上，且转储的文件之和不能超过SATA盘的容量。
# 假设每块SATA盘容量为M，求能转储的最大连续文件大小之和。

# 输入描述：
# 第一行为SATA盘容量M，1000＜=M＜=1000000
# 第二行为区块链文件大小序列F1，F2...Fn。其中1＜=n＜=100000，1＜=Fi＜=500
# 输出描述：
# 求能转储的最大连续文件大小之和
# 示例1 输入输出示例仅供调试，后台判题数据一般不包含示例
# 输入
# 1000
# 100 300 500 400 400 150 100
# 输出
# 950
# 说明
# 最大序列和为950，序列为[400，400，150]

# 示例2输入输出示例仅供调试，后台判题数据一般不包含示例
# 输入
# 1000
# 100 500 400 150 500 100
# 输出
# 1000
# 说明
# 最大序列和为1000，序列为[100，500，400]


def maxSubarr(arr, num):
    """滑动窗口"""
    left = 0
    right = 0
    cur_sum = 0

    max_sum = 0
    max_index = -1
    max_len = 0

    while right < len(arr):
        cur_sum += arr[right]

        # if cur_sum > num:       # 右移过程中第一次大于num
        #     if cur_sum - arr[right] > max_sum:
        #         max_sum = cur_sum - arr[right]
        #         max_index = left
        #         max_len = right - left
            
        while left <= right and cur_sum > num:
            cur_sum -= arr[left]
            left += 1
            
        if cur_sum > max_sum:   # 左移过程中第一次小于等于num
            max_sum = cur_sum
            max_index = left
            max_len = right - left + 1
                
        right += 1

    return max_sum, arr[max_index: max_index + max_len]


if __name__ == '__main__':
    arr = [100, 300, 500, 400, 400, 150, 100]
    num = 1000
    print(maxSubarr(arr, num))
    
    arr = [100, 500, 400, 150, 500, 100]
    num = 1000
    print(maxSubarr(arr, num))
    
