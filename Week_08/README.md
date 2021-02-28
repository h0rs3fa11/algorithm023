学习笔记
### 初级排序python代码
#### 选择排序
```python
def selection_sort(sort_list):
    for i in range(len(sort_list)-1):
        min_index = sort_list.index(min(sort_list[i+1:]))
        sort_list[i], sort_list[min_index] = sort_list[min_index], sort_list[i]
```
#### 插入排序
```python
def insert_sort(sort_list):
    for i in range(1, len(sort_list)):
        value = sort_list[i]
        j = i - 1
        while j >= 0 and value < sort_list[j]:
            sort_list[j+1] = sort_list[j]
            j -= 1
        sort_list[j+1] = value
```
#### 冒泡排序
```python
def bubble_sort(sort_list):
    for i in range(len(sort_list)-1):
        for j in range(i, len(sort_list)):
            if sort_list[j] < sort_list[i]:
                sort_list[i], sort_list[j] = sort_list[j], sort_list[i]

```