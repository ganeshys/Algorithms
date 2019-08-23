def findSmallest(arr):
    smalllest = arr[0]
    smalllest_index = 0
    for i in range(1, len(arr)):  # 从1开始
        if arr[i] < smalllest:
            smalllest = arr[i]
            smalllest_index = i
    return smalllest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)  # 找出最小的元素
        newArr.append(arr.pop(smallest)) # pop作用是移除最小的元素，并将其值返回
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
