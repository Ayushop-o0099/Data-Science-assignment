def count_occurrences(lst):
    for i in set(lst):
        print(f"Count of {i} : {lst.count(i)}")
lst = [1, 2, 2, 3, 4, 4, 4]
count_occurrences(lst)
