def moveZeroes(nums):
    nonZeroIndex = 0

    
    for num in nums:
        if num != 0:
            nums[nonZeroIndex] = num
            nonZeroIndex += 1

    
    while nonZeroIndex < len(nums):
        nums[nonZeroIndex] = 0
        nonZeroIndex += 1


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  
