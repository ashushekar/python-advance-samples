"""
Design a class which receives a list of words in the constructor, and implements
a method that takes two words word1 and word2 and return the shortest distance between
these two words in the list. Your method will be called repeatedly many times with
different parameters.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
"""

class WordDistance:

    def __init__(self, words: List[str]):
        self.length = len(words)
        self.records = {}

        for i, w in enumerate(words):
            self.records.setdefault(w, []).append(i)

    def find(self, nums, n):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            if n < nums[mid]:
                if mid > 0 and nums[mid - 1] < n or mid == 0:
                    return mid
                high = mid - 1
            else:
                low = mid + 1

        return low

    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = map(self.records.get, (word1, word2))

        less, more = l1, l2
        if len(l1) > len(l2):
            less, more = more, less

        distance = self.length
        for i in less:
            index = self.find(more, i)
            if index == 0:
                distance = min(distance, more[index] - i)
            elif index >= len(more):
                distance = min(distance, i - more[-1])
            else:
                distance = min(distance, i - more[index - 1], more[index] - i)

        return distance

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)