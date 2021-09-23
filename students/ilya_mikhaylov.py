def sign_func(nums):
    ans = 1
    for num in nums:
        ans *= num
    if ans == 0:
        return 0
    elif ans > 0:
        return 1
    else:
        return -1
