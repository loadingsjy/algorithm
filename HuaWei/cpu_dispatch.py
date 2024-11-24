# 现有一个CPU和一些任务需要处理，已提前获知每个任务的任务ID、优先级、所需执行时间和到达时间。
# CPU同时只能运行一个任务，请编写一个任务调度程序， 采用“可抢占优先权调度”调度算法进行任务调度，规则如下:
# 1:如果一个任务到来时，CPU是空闲的，则CPU可以运行该任务直到任务执行完毕。但是如果运行中有一个更高优先级的任务到
# 来，则CPU必须暂停当前任务去运行这个优先级更高的任务;
# 2:如果一个任务到来时，CPU正在运行一个比他优先级更高的任务时，信道大的任务必须等待;
# 3:当CPU空闲时，如果还有任务在等待，CPU会从这些任务中选择一个优先级最高的任务执行，相同优先级的任务选择到达时间
# 最早的任务。
# 输入描述
# 输入有若干行，每一行有四个数字(均小于10^8)，分别为任务ID， 任务优先级，执行时间和到达时间。每个任务的任务ID不同，优
# 先级数字越大优先级越高，并且相同优先级的任务不会同时到达。
# 输入的任务已按照到达时间从小到大排序，并且保证在任何时间，处于等待的任务不超过10000个。
# 输出描述
# 按照任务执行结束的顺序，
# 示例一
# 输入
# 1 3 5 1
# 2 1 5 10
# 3 2 7 12
# 4 3 2 20
# 5 4 9 21
# 6 4 2 22
# 输出
# 1 6
# 3 19
# 5 30
# 6 32
# 4 33
# 2 35

import functools

# class task(object):

#     def __init__(self,id,priority,start_time,end_time):
#         self.id = id
#         self.priority = priority
#         self.start_time = start_time
#         self.end_time = end_time

#     def __lt__(self,other):
#         if self.priority == other.priority:
#             return self.start_time > other.start_time
#         else:
#             return self.priority < other.priority


def comp(a, b):
    # 优先级降序，到达时间升序
    if a[1] > b[1]:
        return -1
    elif a[1] == b[1]:
        return a[3] < b[3]
    else:
        return 1


# 找到time时间点的任务
def find_task_by_time(time, tasks):
    res = list()
    for task in tasks:
        if time == task[3]:
            res.append(task)
    return res


def find_task_by_id(id, tasks):
    for task in tasks:
        if task[0] == id:
            return task
    return None


def cpu_dispatch(tasks):
    cpu = None  # 保证cpu每个时刻只有一个或零个任务在进行
    waiting = []  # 等待队列

    time_point = 0
    while len(tasks) > 0:  # 还有有任务没做完
        t = find_task_by_time(time_point, tasks)
        if t:  # 有任务进来
            waiting.extend(t)

        if waiting:
            waiting.sort(key=functools.cmp_to_key(comp))
            if cpu is None:     # cpu空闲，选择一个优先级最高的
                cpu = waiting.pop(0)
            else:               # cpu不空闲，比较优先级
                # 当前来的任务优先级高于cpu正在处理任务的优先级，则抢占
                if waiting[0][1] > cpu[1]:
                    waiting.append(cpu)
                    cpu = waiting.pop(0)

        if cpu is not None:
            cpu[2] -= 1
            if cpu[2] == 0:
                print("id:" + str(cpu[0]) + " task finishing time: " + str(time_point + 1))
                tasks.remove(find_task_by_id(cpu[0], tasks))
                # print(tasks)
                cpu = None

        time_point += 1


if __name__ == "__main__":
    tasks = [
        [1, 3, 5, 1],
        [2, 1, 5, 10],
        [3, 2, 7, 12],
        [4, 3, 2, 20],
        [5, 4, 9, 21],
        [6, 4, 2, 22],
    ]
    
    print(sorted(tasks,key=functools.cmp_to_key(comp)))

    cpu_dispatch(tasks)
