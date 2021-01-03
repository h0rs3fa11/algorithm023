"""
解法1: 数组；设置两个指针front和rear，rear指向最前，每插入一个元素右移一位，每删除一个元素左移一位，front相反；看作循环双端队列front就是前（左）指针，插入后左移删除后右移，rear是右指针，插入后右移删除后左移。
在数组中实现时，修改索引时需要取模
解法2: 双向链表；定义一个链表节点有前指针和后指针，在__init__是建立好整个循环链表，最后同样设置front指针和rear指针。
与数组解法相比，双向链表在__init__初始化时做的工作更多，但其他操作更简单
"""
# 解法1
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = [0] * k
        self.size = 0
        self.capacity = k
        self.front = k - 1
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size >= self.capacity:
            return False
        self.deque[self.front] = value
        self.front = (self.front - 1) % self.capacity
        self.size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.size >= self.capacity:
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.deque[(self.front + 1) % self.capacity] if self.size else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.deque[(self.rear - 1) % self.capacity] if self.size else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.capacity

# 解法2
class MyCircularDeque2:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k
        self.size = 0

        # 第一个节点
        head = Node(0)
        cur = head

        # 初始化循环链表
        for i in range(1, k):
            cur.next = Node(i)
            cur.next.prev = cur
            cur = cur.next
        
        # 设置首尾相连
        cur.next = head
        head.prev = cur

        # 设置前后指针
        self.front = head.prev
        self.rear = head

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size >= self.capacity: return False
        self.front.value = value
        self.front = self.front.prev
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.size >= self.capacity: return False
        self.rear.value = value
        self.rear = self.rear.next
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.size == 0: return False
        self.front = self.front.next
        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.size == 0: return False
        self.rear = self.rear.prev
        self.size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.front.next.value if self.size else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.rear.prev.value if self.size else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.capacity
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None