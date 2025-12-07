sum_joltage = 0

with open("input.txt", "r") as file:
    for line in file:
        nums = list(map(int, line.strip()))
        x1, x2 = nums[0:2]
        for i in range(2, len(nums)):
            if i != len(nums) - 1 and nums[i] > x1:
                x1 = nums[i]
                x2 = nums[i+1]
            else:
                if nums[i] > x2:
                    x2 = nums[i]
        sum_joltage += (x1 * 10) + x2

print(sum_joltage)