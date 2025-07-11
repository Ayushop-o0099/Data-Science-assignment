def majority_element(nums):
    count, candidate = 0, None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    if nums.count(candidate) > len(nums)//2:
        return candidate
    return None
lst = [2, 2, 1, 2, 3, 2, 2]
print("Majority element:", majority_element(lst))
