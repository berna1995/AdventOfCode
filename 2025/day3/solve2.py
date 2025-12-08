sum_joltage = 0

def max_num(nums: list[int], max_digits: int):
    top_num = [0] * max_digits
    top_num_indices = [-1] * max_digits
    for i in range(0, len(nums)):
        for x in range(max_digits):
            if nums[i] > top_num[x] and i <= len(nums) - (max_digits - x) and i > top_num_indices[x]:
                top_num[x:] = nums[i:i+max_digits-x]
                top_num_indices[x:] = list(range(i,i+max_digits-x))
                break
    return int("".join(map(str,top_num)))

with open("input.txt", "r") as file:
    for line in file:
        nums = list(map(int, line.strip()))
        sum_joltage += max_num(nums, 12)
        
print(sum_joltage)
