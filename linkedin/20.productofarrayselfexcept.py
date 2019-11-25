"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal
to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        mult = 1
        for i in range(len(nums)):
            result.append(mult)
            mult = mult * nums[i]

        mult = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * mult
            mult = mult * nums[i]

        return result