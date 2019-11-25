"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if len(points) < 3:
            return n

        maximum = 2
        for i in range(1, n):
            count = 0
            x1 = points[i - 1][0]
            y1 = points[i - 1][1]
            x2 = points[i][0]
            y2 = points[i][1]

            if x1 == x2 and y1 == y2:
                for j in range(n):
                    if points[j][0] == x1 and points[j][1] == x2:
                        count += 1

            else:
                for j in range(n):
                    if (points[j][1] - y2) * (x2 - x1) == (points[j][0] - x2) * (y2 - y1):
                        count += 1

            maximum = max(maximum, count)

        return maximum