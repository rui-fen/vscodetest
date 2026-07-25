# vscodetest

Python 实现的冒泡排序示例，用于演示基础排序算法与提前退出优化。

## 功能

- `bubble_sort(numbers)`：对输入列表进行升序排序，**不修改原列表**，返回新列表
- 若某一轮比较中没有发生交换，则提前结束（列表已有序）

## 环境要求

- Python 3.6+

## 使用

```bash
python bubble_sort.py
```

示例输出：

```
[2, 3, 4, 5, 8]
```

在代码中调用：

```python
from bubble_sort import bubble_sort

sorted_list = bubble_sort([5, 3, 8, 4, 2])
```

## 算法说明

冒泡排序重复遍历列表，比较相邻元素并在顺序错误时交换。每轮结束后，当前未排序部分中的最大值会“冒泡”到末尾。本实现带有 `swapped` 标志：当一轮内无交换时，说明已全部有序，可立即停止。

## 许可

按需自行使用与修改。
