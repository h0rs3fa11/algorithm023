学习笔记

### 双端BFS代码模版
```python
def bfs_search(begin, end):
    begin_queue = collections.deque([begin])
    end_queue = collections.deque([end])
    visited = set()
    while begin_queue:
        # 开始当前层
        current = len(begin_queue)
        for _ in range(current):
            value = begin_queue.popleft()
            if value not in visited:
                # 处理begin_queue队列元素value
                # ...
                # 判断中间值是否在end_queue中
                if value in end_queue:
                    return
                # 中间值添加到已访问列表
                visited.add(value)
                # 更新begin_queue
                begin_queue.append(value)
        # 设置较小队列为begin_queue
        if len(begin_queue) > len(end_queue):
            begin_queue, end_queue = end_queue, begin_queue
    return -1
```