def second_largest(lst):
    unique_lst = list(set(lst))
    if len(unique_lst) < 2:
        return None
    unique_lst.sort()
    return unique_lst[-2]
lst = [10, 20, 4, 45, 99]
print("Second largest number is:", second_largest(lst))
