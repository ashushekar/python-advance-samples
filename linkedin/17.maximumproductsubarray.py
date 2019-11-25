"""
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -float('inf')
        product = 1
        length = len(nums)
        for i in range(length):
            product *= nums[i]
            res = max(product, res)
            if nums[i] == 0:
                product = 1
        # scan backward
        product = 1
        for j in range(length - 1, -1, -1):
            product *= nums[j]
            res = max(product, res)
            if nums[j] == 0:
                product = 1
        return res