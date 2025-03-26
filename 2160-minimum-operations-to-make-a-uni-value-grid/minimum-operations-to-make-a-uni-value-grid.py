class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten and sort the input array
        nums = [num for row in grid for num in row]
        
        # Fast early exit checks
        if not nums:
            return 0
        
        # Check remainder consistency
        base_remainder = nums[0] % x
        if any(num % x != base_remainder for num in nums):
            return -1
        
        # Sort the array
        nums.sort()
        n = len(nums)
        
        # Find median for minimum operations
        median = nums[n // 2]
        
        # Calculate total operations
        total_ops = sum(abs(num - median) // x for num in nums)
        
        return total_ops
        
        return total_ops