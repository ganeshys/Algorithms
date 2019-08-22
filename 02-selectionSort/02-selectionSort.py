def findSmallest(arr):
    smalllest = arr[0]
    smalllest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smalllest:
            smalllest = arr[i]
            smalllest_index = i
    return smalllest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
