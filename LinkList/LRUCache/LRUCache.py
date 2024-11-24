# LRU缓存
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。
# 如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
# 示例：
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/lru-cache/solutions/2456294/tu-jie-yi-zhang-tu-miao-dong-lrupythonja-czgt/

"""这里是一个双向循环链表，不是一个单纯的双向链表。 
1)双向链表（Doubly Linked List）：
在双向链表中，每个节点都有两个指针，一个指向前一个节点，一个指向后一个节点。 
双向链表有一个明确的头节点和尾节点，尾节点的后继指针通常指向 null（或 None），表示链表的结束。 
在双向链表中，遍历从头节点或尾节点开始，可以很容易地在任意方向上进行插入和删除操作。 
2)双向循环链表（Doubly Circular Linked List）：
在双向循环链表中，最后一个节点的后继指针指向第一个节点，形成一个循环。 
由于循环性质，双向循环链表在遍历时不需要考虑链表的结束，因为可以从任何一个节点出发绕过整个链表。 
双向循环链表通常没有明确的头节点和尾节点，可以选择任意一个节点作为起点。

总结一下： 
1.两个数据结构，双向循环链表和哈希表 
2.需要自己自定义双向循环链表和其基本操作删除和插入操作 
3.定义get_node API，这个才是这个复合数据结构的操作，剩下就是记得怎么更新双向循环链表和哈希表了

额外说下dummy的作用： 
1.快速找到双向循环链表中最末尾的节点 
2.插入时，快速找到最新位置 
3.操作可以不区分head节点和tail节点，让其更普通节点一样

总结：同化了head节点和tail节点的操作，要提供了快速找到head和tail的方法。额外的一点空间却极大简化的操作。妙！"""


class Node:
    # 提高访问属性的速度，并节省内存
    __slots__ = "prev", "next", "key", "value"

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()  # 哨兵节点
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = dict()

    def get_node(self, key: int):
        if key not in self.key_to_node:  # 没有这本书
            return None
        node = self.key_to_node[key]  # 有这本书
        self.remove(node)  # 把这本书抽出来
        self.push_front(node)  # 放在最上面
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)  # get_node方法已经把书放在最上面了
        if node:  # 有这本书
            node.value = value  # 更新 value
            return
        self.key_to_node[key] = node = Node(key, value)  # 新书
        self.push_front(node)  # 放在最上面
        if len(self.key_to_node) > self.capacity:  # 书太多了
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)  # 去掉最后一本书

    # 删除一个节点（抽出一本书）
    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev

    # 在链表头添加一个节点（把一本书放在最上面）
    def push_front(self, x: Node) -> None:
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x


if __name__ == "__main__":
    capacity = 4
    obj = LRUCache(capacity)
    obj.put(1, 4)
    obj.put(2, 5)
    obj.put(3, 7)
    obj.put(4, 2)
    obj.put(5, 0)
    obj.put(6, 12)
    param_1 = obj.get(2)
    param_2 = obj.get(3)
    param_3 = obj.get(6)
    obj.put(2, 6)
    param_4 = obj.get(2)
    print(param_1, param_2, param_3, param_4)
