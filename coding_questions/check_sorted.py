def is_sorted(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)
lst = [1, 2, 3, 4, 5]
print("Is list sorted : ",is_sorted(lst))
