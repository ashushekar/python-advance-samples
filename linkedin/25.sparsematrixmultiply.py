"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

class Solution:
    def compress(self, matrix):
        return [
            [i, j, num]
            for i, row in enumerate(matrix)
            for j, num in enumerate(row) if num
        ]

    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        (cpA, cpB) = map(self.compress, (A, B))

        result = [[0] * len(B[0]) for i in range(len(A))]

        [result[rowA].__setitem__(columnB, result[rowA][columnB] + numA * numB)
         for rowA, columnA, numA in cpA
         for rowB, columnB, numB in cpB if columnA == rowB]

        return result
