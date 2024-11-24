#
# * 27. 移除元素

# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
# 假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：
# 更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
# 返回 k。


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """初始化要填入的下标k=0；
        从左到右遍历 nums，如果 nums[i]==val，则更新 nums[k]=nums[i]，然后把 k 加一；
        遍历结束，返回 k。"""
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k

    def removeElement2(self, nums: list[int], val: int) -> int:
        """双指针法：
        由于题目要求删除数组中等于 val 的元素，因此输出数组的长度一定小于等于输入数组的长度，我们可以把输出的数组直接写在输入数组上。
        可以使用双指针：右指针 right 指向当前将要处理的元素，左指针 left 指向下一个将要赋值的位置。
        如果右指针指向的元素不等于 val，它一定是输出数组的一个元素，我们就将右指针指向的元素复制到左指针位置，然后将左右指针同时右移；
        如果右指针指向的元素等于 val，它不能在输出数组里，此时左指针不动，右指针右移一位。
        整个过程保持不变的性质是：区间 [0,left) 中的元素都不等于 val。当左右指针遍历完输入数组以后，left 的值就是输出数组的长度。
        这样的算法在最坏情况下（输入数组中没有元素等于 val），左右指针各遍历了数组一次。"""
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
                right += 1
            else:
                right += 1
        return left

    def removeElement2(self, nums: list[int], val: int) -> int:
        """双指针优化：
        如果左指针 left 指向的元素等于 val，此时将右指针 right 指向的元素复制到左指针 left 的位置，然后右指针 right 左移一位。
        如果赋值过来的元素恰好也等于 val，可以继续把右指针 right 指向的元素的值赋值过来（左指针 left 指向的等于 val 的元素的位置继续被覆盖），直到左指针指向的元素的值不等于 val 为止。
        当左指针 left 和右指针 right 重合的时候，左右指针遍历完数组中所有的元素。
        这样的方法两个指针在最坏的情况下合起来只遍历了数组一次。与方法一不同的是，方法二避免了需要保留的元素的重复赋值操作。"""
        n = len(nums)
        left, right = 0, n - 1
        while right >= left:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left
