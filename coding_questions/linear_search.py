def linear_search(lst, target):
    i=0
    for val in lst:
        if val == target:
            return i
        i=i+1
    return -1

lst = [5, 3, 7, 1, 9]
target = 7
print("Element found at index:", linear_search(lst, target))
