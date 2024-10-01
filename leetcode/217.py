
def duplicate():
    nums = [2, 14, 18, 22, 22]
    if len(nums) == 1:
        return False
    else:
        nums = sorted(nums)
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


print(duplicate())
