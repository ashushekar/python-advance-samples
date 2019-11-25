"""

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
"""

import math


class Solution:
    def getFactors(self, n: int, start: int = 2) -> List[List[int]]:

        result = []
        sqrt = lambda x: int(math.sqrt(x))
        for i in range(start, sqrt(n) + 1):
            div, mod = divmod(n, i)
            if not mod:
                result = result + [[i, div]]
                if sqrt(div) >= i:
                    result = result + [[i] + p for p in self.getFactors(div, i)]

        return result