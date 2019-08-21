def  binary_search(list,item):
     low = 0
     high = len(list-1)
     
     while low < high:
        mid = (low + high) // 2   # 在python3中所有除法结果都是float
                                 #如果你想执行象C语言那样的整数除法，必须使用//这个操作符
        guess = list[mid]
        if guess == item:
           return mid
        if guess > item:
           high = mid - 1    #item在中间数左边，移动high下标
        else:
           low = mid + 1   #item在中间数右边，移动low下标
        return None
        
 my_list=[1,3,5,7,9]
print(binary_search(my_list, 3))  #  =>1
print(binary_search(my_list, -1)) #  =>None