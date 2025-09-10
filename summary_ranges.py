def summary_ranges(nums: list):
    n = len(nums)
    answer = []
    i = 0

    while i < n:
        j = i
        while j + 1 < n and nums[j + 1] == nums[j] + 1:
            j += 1
        
        if i == j:
            answer.append(str(nums[i]))
        else:
            answer.append(str(nums[i]) + "->" + str(nums[j]))
        
        i = j + 1
    
    return answer


print(summary_ranges([0, 1, 2, 4, 5, 7]))