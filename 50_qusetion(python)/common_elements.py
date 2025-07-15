def common(l1, l2):
    return list(set(l1) & set(l2))

print(common([1, 2, 3], [2, 3, 4]))