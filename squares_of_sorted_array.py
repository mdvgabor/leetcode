def sorted_squares(nums):
    left = 0
    right = len(nums) - 1
    result = []

    while left <= right:
        if abs(nums[left]) < abs(nums[right]):
            result.append(nums[right]**2)
            right -= 1
        else:
            result.append(nums[left]**2)
            left += 1

    result.reverse()
    return result

print(sorted_squares([-4, -1, 0, 3, 10]))
