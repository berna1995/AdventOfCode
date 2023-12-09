import sys


def get_extrapolated_value(input: str) -> int:
    nums = list(reversed(list(map(int, input.strip().split(' ')))))
    diffs = [nums[i] - nums[i-1] for i in range(1, len(nums))]
    diff_sum = diffs[-1]

    while any(diffs[i] != diffs[0] for i in range(1, len(diffs))):
        diffs = [diffs[i] - diffs[i-1] for i in range(1, len(diffs))]
        diff_sum += diffs[-1]

    return nums[-1] + diff_sum


with open(sys.argv[1], 'r') as file:
    print(sum(get_extrapolated_value(line) for line in file))
