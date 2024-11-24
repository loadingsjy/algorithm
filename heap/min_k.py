#  最小的k个数
import heapq


class Solution:
    def getLeastNumbers(self, arr: list[int], k: int) -> list[int]:
        if k == 0:
            return []
        # python中只有最小堆，没有最大堆
        # 将所有元素取反，弹出的时候也取反
        heap = [-x for x in arr[0:k]]
        heapq.heapify(heap)
        for x in arr[k:]:
            if -x > heap[0]:
                heapq.heapreplace(heap,-x)
        return [-x for x in heap]
    
    
if __name__ == '__main__':
    arr = [4,5,6,2,7,3,8,9]
    k = 4
    s = Solution()
    print(s.getLeastNumbers(arr, k)) # [1,2,3,4]
