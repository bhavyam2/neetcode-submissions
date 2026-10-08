class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        previous = node.prev
        following = node.next

        previous.next = following

        following.prev = previous

    def _add_most_recent(self, node: Node) -> None:

        previous = self.tail.prev
        node.prev = previous
        node.next = self.tail

        previous.next = node
        self.tail.prev = node
    
    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._remove(node)
        self._add_most_recent(node)

        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._remove(node)
            self._add_most_recent(node)

            return
        node = Node(key, value)
        self.nodes[key] = node
        self._add_most_recent(node)

        if len(self.nodes) > self.capacity:
            oldest = self.head.next
            self._remove(oldest)
            del self.nodes[oldest.key]

        

