# 题目描述:
# 有5台打印机打印文件，每台打印机有自己的待打印队列9。因为打印的文件内容有轻重缓急之分，
# 所以队列中的文件有1~10不同的代先级，其中数字越大优先级越高。
# 打印机会从自己的待打印队列中选择优先级最高的文件来打印。
# 如果存在两个优先级Q-样的文件，则选择最早进入队列的那个文件。
# 现在请你来模拟这5台打印机的打印过程。
# 输入描述:
# 每个输入包含1个测试用例，每个测试用例第一行给出发生事件的数量N (0<N< 1000)。
# 接下来有N行，分别表示发生的事件。
# 共有如下两种事件:
# 1.“IN P NUM"，表示有一个拥有优先级NUM的文件放到了打印机P的待打印队列中。(0<P<=5, 0< NUM <= 10);
# 2. "OUTP”,表示打印机P进行了一次文件打印，同时该文件从待打印队列中取出。(0<P<=5) 。
# 输出描述:
# 对于每个测试用例，每次"OUT P”事件，请在一行中输出文件的编号。
# 如果此时没有文件可以打印，请输出"NULL"。
# 文件的编号定义为"IN P NUM"事件发生第X次，此处待打印文件的编号为x。编号从1开始。
# 示例1输入输出示例仅供调试， 后台判断数据一般不包含示例
# 输入
# IN1 1
# IN1 2
# IN1 3
# IN2 1
# OUT 1
# OUT 2
# OUT 2
# 输出
# 3
# 4
# NULL

import heapq
from queue import PriorityQueue

# class PriorityQueue(object):
#     '''优先级队列'''
#     def __init__(self):
#         self.__queue = []
#         self.__index = 0

#     def is_empty(self):
#         if len(self.__queue) == 0:
#             return True
#         return False
        
#     def push(self, item, priority):
#         heapq.heappush(self.__queue, (-priority, self.__index, item))
#         # 第一个参数：添加进的目标序列
#         # 第二个参数：将一个元组作为整体添加进序列，目的是为了方便比较
#         # 在priority相等的情况下，比较_index
#         # priority为负数使得添加时按照优先级从大到小排序，因为堆排序的序列的第一个元素永远是最小的
#         self.__index += 1
        
#     def pop(self):
#         if self.is_empty():
#             raise IndexError('优先级队列为空，不能弹出')
#         # 返回按照-priority 和 _index 排序后的第一个元素(是一个元组)的最后一个元素(item)
#         return heapq.heappop(self.__queue)[-1]
    
    
if __name__ == '__main__':
    n = int(input())
    machine2Queue = dict()
    answer = []
    for i in range(n):
        line = input().strip().split()
        action = line[0]
        machine_index = int(line[1])
        
        if len(line) == 3:
            priority = int(line[2])
            
        if action == 'IN':
            if machine_index in machine2Queue:
                machine2Queue[machine_index].put((-priority, i+1))
            else:
                q = PriorityQueue()     # 每台打印机为一个优先级队列
                machine2Queue[machine_index] = q
                q.put((-priority, i + 1))
        elif action == 'OUT':
            if machine_index in machine2Queue:
                if machine2Queue[machine_index].empty():
                    answer.append('NULL')
                else:
                    answer.append(str(machine2Queue[machine_index].get()[1]))

    print('\n'.join(answer))

    
    

