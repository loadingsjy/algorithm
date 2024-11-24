# 实时获得数据流中找中位数


import heapq
class MedianFinder:
 
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = [] # 最大堆保存的是最小的n/2个数
        self.minHeap = [] # 最小堆保存的是最大的n/2个数
 
    def addNum(self, num: int) -> None:
        # 若两堆的数目相等，就让minHeap的元素个数+1
        # 具体做法分为两步 1.将新元素加入maxHeap 2.将maxHeap的堆顶元素加入minHeap
        if len(self.maxHeap)==len(self.minHeap):
            heapq.heappush(self.minHeap,-heapq.heappushpop(self.maxHeap,-num))
        else:
            heapq.heappush(self.maxHeap,-heapq.heappushpop(self.minHeap,num))
            
    def findMedian(self) -> float:
        if len(self.maxHeap)==len(self.minHeap):
            return (self.minHeap[0]-self.maxHeap[0])/2.0
        else:
            return self.minHeap[0]


# Example usage:
if __name__ == '__main__':
    medianFinder = MedianFinder()
    nums = [1,2,3,4,5,6,7,8,9,10]
    for num in nums:
        medianFinder.addNum(num)
        print(medianFinder.findMedian())
