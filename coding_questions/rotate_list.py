def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

lst = [1, 2, 3, 4, 5]
k = 2
print("Rotated list:", rotate_list(lst, k))
