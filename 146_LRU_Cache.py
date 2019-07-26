class DLinkedNode():

    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class Solution():
    
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def _pop_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def __init__(self, capacity):
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.cache = {}
        self.size = 0
        self.capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        node = self.cache.get(key, None)
        if node:
            self._move_to_head(node)
            return node.value
        return -1
    
    def put(self, key, value):
        node = self.cache.get(key, None)

        if not node:
            node = DLinkedNode()
            node.key = key
            node.value = value
            self._add_node(node)
            self.cache[key] = node
            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            node._move_to_head(node)
