def max_number(*nums):
    num_list = list(nums)
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num


print(max_number(93, 9, 6, 12, 145, 2, 5, 89))
