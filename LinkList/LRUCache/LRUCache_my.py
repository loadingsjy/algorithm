class Node:
    __slots__ = ("key", "value", "next", "prev")

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity  # 固定变量，缓存容量
        self.size = 0  # 当前使用缓存的容量
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.key_to_node = dict()

    def get(self, key: int) -> int:
        node = self.get_node(key)
        if node is None:
            return -1
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node is not None:
            node.value = value
            return
        x = Node(key, value)
        self.key_to_node[key] = x
        self.front_insert(x)
        self.size += 1
        if self.size > self.cap:
            # 删除最后一个节点，以及字典对应的map
            last_node = self.dummy.prev
            self.remove_node(last_node)
            del self.key_to_node[last_node.key]
            self.size -= 1

    def get_node(self, key):
        """查找关键字为key的节点，如果没有，则返回None，如果有，则将节点放到最上面"""
        if key not in self.key_to_node:
            return None
        x = self.key_to_node[key]
        self.remove_node(x)
        self.front_insert(x)
        return x

    def front_insert(self, node):
        """在链表开头插入节点node"""
        node.prev = self.dummy
        node.next = self.dummy.next
        self.dummy.next.prev = node
        self.dummy.next = node

    def remove_node(self, node):
        """删除node节点"""
        node.prev.next = node.next
        node.next.prev = node.prev


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
