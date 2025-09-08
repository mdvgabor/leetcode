def closest_num_to_zero(nums):
    closest = nums[0]
    for x in nums:
        if abs(x) < abs(closest):
            closest = x
        if abs(x) == abs(closest) and x > closest:
            closest = x
    return closest

print(closest_num_to_zero([-4, -2, 1, 4, 2]))