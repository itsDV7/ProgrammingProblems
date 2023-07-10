def largestnum(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j]+nums[i] >= nums[i]+nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return int(''.join(nums))
if __name__ == "__main__":
    n = int(input())
    nums = input().split()
    print(largestnum(nums))
