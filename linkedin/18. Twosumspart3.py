class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        nums = self.nums
        low = 0
        high = len(nums) - 1
        index = len(nums)
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] < number:
                low = mid + 1
            else:
                if (mid == 0) or (mid > 0 and nums[mid - 1] < number):
                    index = mid
                    break
                high = mid - 1

        nums.insert(index, number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        nums = self.nums
        low, high = 0, len(nums) - 1

        while low < high:
            s = nums[low] + nums[high]
            if s < value:
                low += 1
            elif s > value:
                high -= 1
            else:
                return True

        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)