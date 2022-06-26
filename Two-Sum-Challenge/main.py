import random


def two_sum(nums, target):
    index_list = []
    increment = 0
    end_list = []
    k = True
    other_list = []

    for index in nums:
        index_list.append(increment)
        increment += 1

    while k:
        x = random.choice(index_list)
        y = random.choice(index_list)
        if nums[x] + nums[y] == target and x != y:
            end_list.append(x)
            end_list.append(y)
            end_list.sort()
            k = False
            return end_list


print(two_sum([2,7,11,15], 9))
