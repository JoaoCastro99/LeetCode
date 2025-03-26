class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # 1. Check all remainders
        # 2. Flatten and sort the input
        # 3. Prefix sum / suffix sum

        total = 0
        for row in grid:
            for n in row:
                total += n
                if n % x != grid[0][0] % x:
                    return -1

        nums = [n for row in grid for n in row ]
        nums.sort()

        prefix = 0
        res = float('inf')

        for i in range(len(nums)):
            cost_left = nums[i] * i - prefix
            cost_right = total - prefix - (nums[i] * (len(nums) - i))
            operations = (cost_left + cost_right) // x
            res = min(res, operations)
            prefix += nums[i]
        return res             