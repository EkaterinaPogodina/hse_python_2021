def num_identical_pairs(nums):
    counter = 0
    for i in range(0, len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                counter += 1
    return counter
