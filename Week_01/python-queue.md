https://github.com/python/cpython/blob/3.9/Lib/queue.py
### Python Queue

python的queue是线程安全的，此处略过一些有关线程同步的代码

```python
class Queue:
    '''Create a queue object with a given maximum size.

    If maxsize is <= 0, the queue size is infinite.
    '''

    def __init__(self, maxsize=0):
        self.maxsize = maxsize
        self._init(maxsize)
    
    def qsize(self):
        with self.mutex:
            return self._qsize()
    
    def empty(self):
        with self.mutex:
            return not self._qsize()
    
    def full(self):
        with self.mutex:
            return 0 < self.maxsize <= self._qsize()

    def put_nowait(self, item):
        return self.put(item, block=False)
    
    def get_nowait(self):
        return self.get(block=False)

    def _init(self, maxsize):
        # 定义了一个deque
        self.queue = deque()

    def _qsize(self):
        # 返回队列的长度
        return len(self.queue)

    # Put a new item in the queue
    def _put(self, item):
        # 在队列后append
        self.queue.append(item)

    # Get an item from the queue
    def _get(self):
        # 调用deque的popleft方法，，返回左边元素
        return self.queue.popleft()
```

### Python Priority Queue
python使用heapq实现优先队列，heapq有几个函数
```python
class PriorityQueue(Queue):
    '''Variant of Queue that retrieves open entries in priority order (lowest first).

    Entries are typically tuples of the form:  (priority number, data).
    '''
    # 初始化空列表
    def _init(self, maxsize):
        self.queue = []
    # 返回列表长度
    def _qsize(self):
        return len(self.queue)
    # 调用heapq的heappush函数
    def _put(self, item):
        heappush(self.queue, item)
    # 调用heapq的heappop函数
    def _get(self):
        return heappop(self.queue)
```

- `heapq.heappush(heap, item)` 堆插入元素
- `heapq.heappop(heap) `堆删除最小元素

### 堆的插入

二叉堆是一颗完全二叉树，插入一个元素首先将它追加到二叉树的末尾，再依次跟父节点比较，如果小于父节点，当前元素就往上走，与父节点交换，依次向上直到根节点。

由于是完全二叉树，所以可以用list来保存，i的子节点是`2*i+1`和`2*i+2`，父节点是`(i-1)/2`

```python
def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)
```

首先将item追加到heap，再调用`_siftdown`调整当前的堆

```python
def _siftdown(heap, startpos, pos):
    # startpos是根节点
    # 堆末尾元素， 即新元素
    newitem = heap[pos]
    # 当pos未到根节点
    while pos > startpos:
        # 找到节点的父节点
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        # 如果新元素小于父节点
        if newitem < parent:
            # 将父节点下移变成子节点
            heap[pos] = parent
            # 当前位置更新为父节点位置
            pos = parentpos
            continue
        break
    # 将新元素的值赋值给计算完的位置
    heap[pos] = newitem
```

### 删除最小值

最小值是根节点，但是不能直接删除根节点破坏堆结构，把末尾节点移动到根节点，再依次调整：从两个子节点中选一个更小的作为根节点，依次向下直到叶子节点

```python
def heappop(heap):
    # 弹出最后一个元素赋值给lastelt
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        # lateslt赋值给根节点
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt
```

`_siftup`调整当前堆

```python
def _siftup(heap, pos):
    # 末尾位置
    endpos = len(heap)
    # 起始位置，这里是根节点
    startpos = pos
    newitem = heap[pos]
    # 将更小的元素冒泡上来，直到叶子节点
    childpos = 2*pos + 1    # 左子节点位置
    # while 未达到叶子节点
    while childpos < endpos:
        # 右子节点位置
        rightpos = childpos + 1
        # 右子节点也未到叶子节点，并且左子节点大于等于右子节点（这一步从两个字节点中选出最小的赋值给childpos）
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # 将较小的子节点往上移动
        heap[pos] = heap[childpos]
        # 调整当前pos位置
        pos = childpos
        childpos = 2*pos + 1
    # 将新元素放在pos的位置
    heap[pos] = newitem
    # 调用_siftdown，与插入操作一样，最后调整新元素的位置
    _siftdown(heap, startpos, pos)
```