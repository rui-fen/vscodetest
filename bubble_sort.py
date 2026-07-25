def bubble_sort(numbers):
    """使用冒泡排序返回一个升序的新列表。"""
    result = numbers.copy()
    n = len(result)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        # 若本轮没有交换，列表已经有序。
        if not swapped:
            break

    return result


if __name__ == "__main__":
    data = [5, 3, 8, 4, 2]
    print(bubble_sort(data))  # [2, 3, 4, 5, 8]
