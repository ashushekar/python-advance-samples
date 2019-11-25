"""
Given a list of words and two words word1 and word2, return the shortest
distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
"""

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        last_word1 = None
        last_word2 = None
        distance = len(words)

        for i, w in enumerate(words):
            if w == word1:
                if last_word2 is not None and i - last_word2 < distance:
                    distance = i - last_word2
                last_word1 = i

            if w == word2:
                if last_word1 is not None and i - last_word1 < distance:
                    distance = i - last_word1
                last_word2 = i

        return distance