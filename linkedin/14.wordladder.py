"""

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""

from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or beginWord == endWord:
            return 0

        one_diff = defaultdict(list)

        for word in wordList:
            for i, _ in enumerate(word):
                key = word[:i] + "*" + word[i + 1:]
                one_diff[key].append(word)

        # print(one_diff)
        begin = [beginWord]
        visited = set()
        level = 1
        while begin:
            for i in range(len(begin)):
                word = begin.pop(0)
                for i, _ in enumerate(word):
                    key = word[:i] + "*" + word[i + 1:]
                    for word2 in one_diff[key]:
                        if word2 != word and word2 not in visited:
                            if word2 == endWord:
                                return level + 1
                            visited.add(word2)
                            begin.append(word2)

            level = level + 1
        return 0
