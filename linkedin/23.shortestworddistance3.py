"""
Given a list of words and two words word1 and word2, return the shortest
distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words
in the list.
"""

class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        distance = len(words)

        if word1 != word2:
            last_word1, last_word2 = None, None
            for i, w in enumerate(words):
                if w == word1:
                    if last_word2 is not None and i - last_word2 < distance:
                        distance = i - last_word2
                    last_word1 = i

                if w == word2:
                    if last_word1 is not None and i - last_word1 < distance:
                        distance = i - last_word1
                    last_word2 = i
        else:
            last = None
            for i, w in enumerate(words):
                if w == word1:
                    if last is not None and i - last < distance:
                        distance = i - last
                    last = i

        return distance