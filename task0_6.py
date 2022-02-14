def max_number(*nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


print(max_number(93, 9, 6, 12, 145, 2, 5, 89))
