def move_zeros(lst):
    non_zeros = [x for x in lst if x != 0]
    return non_zeros + [0]*(len(lst) - len(non_zeros))

# Example
lst = [0, 1, 0, 3, 12]
print("After moving zeros:", move_zeros(lst))
