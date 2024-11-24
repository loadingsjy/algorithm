import heapq

class PriorityQueue:
    def __init__(self):
        self.__queue = []
        self.__index = 0
        
    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        return False
        
    def push(self, item, priority):
        heapq.heappush(self.__queue, (-priority, self.__index, item))
        # 第一个参数：添加进的目标序列
        # 第二个参数：将一个元组作为整体添加进序列，目的是为了方便比较
        # 在priority相等的情况下，比较_index
        # priority为负数使得添加时按照优先级从大到小排序，因为堆排序的序列的第一个元素永远是最小的
        self.__index += 1
        
    def pop(self):
        if self.is_empty():
            raise IndexError('优先级队列为空，不能弹出')
        # 返回按照-priority 和 _index 排序后的第一个元素(是一个元组)的最后一个元素(item)
        return heapq.heappop(self.__queue)[-1]



if __name__ == '__main__':
    q = PriorityQueue()
    q.push("bar", 2)
    q.push("foo", 1)
    q.push("gork", 3)
    q.push("new", 1)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    # print(q.pop())
    
    """
    gork  # 优先级最高
    bar   # 优先级第二
    foo   # 优先级与new相同，比较index，因为先加入，index比new小，所以排在前面
    new
    """