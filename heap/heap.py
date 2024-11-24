"""堆是一个完全二叉树，其中每个节点的值都大于或等于其子节点的值。
优先级队列就是堆结构的应用。

堆：完全二叉树，每个节点的值都大于或等于其子节点的值，称为最大堆或大根堆；每个节点的值都小于或等于其子节点的值，称为最小堆或小根堆。
大顶堆：每个节点的值都大于其子节点的值，即根节点的值最大。
小顶堆：每个节点的值都小于其子节点的值，即根节点的值最小。

完全二叉树的性质  1. 除了最底层，其他层的节点都有两个子节点；
                 2. 最底层的叶子节点都在同一层上，最后一层从左到右的顺序为1, 2, 3, 4, 5, 6, 7, 8, 9, 10

用数组存储完全二叉树，数组的索引从0开始，数组的元素值表示节点的值。
若父节点的索引为i，则其左子节点的索引为2i+1，右子节点的索引为2i+2。
若子节点的索引为i，则其父节点的索引为(i-1)//2。
若数组的长度为n，则其最后一个非叶子节点的索引为(n-2)//2。

堆结构的应用：
堆可以用来实现图的最小生成树算法，堆可以用来实现堆排序算法，堆可以用来实现堆栈和队列。
"""

# 本代码是堆数据结构的简单实现。它支持最小堆和最大堆。
# 该实现基于heapify算法，这是一种维护堆属性的递归算法。
# heapify_down函数用于从第i个节点开始，在堆中从上往下堆化。
# heapify_up函数用于从第i个节点开始，在堆中从下往上堆化。
# insert函数用于向堆中添加元素。
# change_value函数用于改变堆中元素的值。
# peek函数用于获得堆顶元素的值。
# pop函数用于删除堆顶元素。


class Heap:
    def __init__(self, is_max_heap=True):
        self.heap = []
        self.is_max_heap = is_max_heap

    def build_heap(self, arr):
        """构造堆"""
        self.heap = arr
        n = len(arr)
        for i in range((n - 2) // 2, -1, -1):
            self.heapify_down_no_recursive(i)

    def heapify_up(self, index):
        parent = (index - 1) // 2
        if self.is_max_heap:
            if parent >= 0 and self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index],
                )
                self.heapify_up(parent)
        else:
            if parent >= 0 and self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index],
                )
                self.heapify_up(parent)

    def heapify_up_no_recursive(self, i):
        """从第i个节点开始，从下往上堆化"""
        if self.is_max_heap:
            while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
                self.heap[i], self.heap[(i - 1) // 2] = (
                    self.heap[(i - 1) // 2],
                    self.heap[i],
                )
                i = (i - 1) // 2
        else:
            while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
                self.heap[i], self.heap[(i - 1) // 2] = (
                    self.heap[(i - 1) // 2],
                    self.heap[i],
                )
                i = (i - 1) // 2

    def heapify_down(self, index):
        n = len(self.heap)
        left = 2 * index + 1
        right = 2 * index + 2
        if self.is_max_heap:
            largest = index
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != index:
                self.heap[index], self.heap[largest] = (
                    self.heap[largest],
                    self.heap[index],
                )
                self.heapify_down(largest)
        else:
            smallest = index
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != index:
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index],
                )
                self.heapify_down(smallest)

    def heapify_down_no_recursive(self, i):
        """从第i个节点开始，从上往下堆化"""
        n = len(self.heap)
        dad = i
        son = 2 * i + 1  # left son

        while son < n:
            if self.is_max_heap:
                # find the greater son
                if son + 1 < n and self.heap[son + 1] > self.heap[son]:
                    son += 1
                # swap if son is greater than dad
                if self.heap[son] > self.heap[dad]:
                    self.heap[son], self.heap[dad] = self.heap[dad], self.heap[son]
            else:
                # find the smaller son
                if son + 1 < n and self.heap[son + 1] < self.heap[son]:
                    son += 1
                # swap if son is smaller than dad
                if self.heap[son] < self.heap[dad]:
                    self.heap[son], self.heap[dad] = self.heap[dad], self.heap[son]

            dad = son
            son = 2 * son + 1

    def insert(self, value):
        """新来的元素默认放在最后面，然后从最后面的元素开始往上堆化"""
        self.heap.append(value)
        self.heapify_up_no_recursive(len(self.heap) - 1)

    # def change_value(self, index, new_value):
    #     '''第index个元素的值变为new_value，改变堆中元素的值，并保持堆的性质'''
    #     if self.heap[index] == new_value:
    #         return
    #     self.heap[index] = new_value
    #     self.heapify_up_no_recursive(index)
    #     self.heapify_down_no_recursive(index)

    def peek(self):
        """获得堆顶元素的值"""
        return self.heap[0]

    def pop(self):
        """删除堆顶元素，并保持堆的性质"""
        top = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()  # remove the last element
        self.heapify_down_no_recursive(0)
        return top


# test
if __name__ == "__main__":
    # max heap
    heap = Heap(is_max_heap=True)
    heap.build_heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    print("original max heap: ", heap.heap)

    heap.insert(15)
    print("insert 15: ", heap.heap)

    heap.change_value(3, 3)
    print("change_value: ", heap.heap)

    print("top value: ", heap.pop())
    print("pop top: ", heap.heap)

    # min heap
    heap_1 = Heap(is_max_heap=False)
    heap_1.build_heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    print("\n\n\noriginal min heap: ", heap_1.heap)

    heap_1.insert(3)
    print("insert 15: ", heap_1.heap)

    heap_1.change_value(3, 11)
    print("change_value: ", heap_1.heap)

    print("top value: ", heap_1.pop())
    print("pop top: ", heap_1.heap)
