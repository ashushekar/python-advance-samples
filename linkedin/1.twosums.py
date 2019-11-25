"""
/**
 * Created by rbhatnagar2 on 1/12/17.
 *
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 *
 * You may assume that each input would have exactly one solution,
 * and you may not use the same element twice.
 *
 * Example:
 *
 * Given nums = [2, 7, 11, 15], target = 9,
 *
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 *
 */

 """

def operation(nums, target):
    dictA = {}

    for i in range(len(nums)):
        second = target - nums[i]
        if second in dictA.keys():
            return dictA[second], i

        else:
            dictA[nums[i]] = i

    return None

def ifsorted(nums, target):
    start = 0
    end = len(nums) - 1

    while start < end:
        compute = nums[start] + nums[end]

        if target == compute:
            return start, end
        elif target < compute:
            end -= 1
        else:
            start += 1

    return None

nums = [11, 7, 2, 15]
target = 9
print(operation(nums, target))