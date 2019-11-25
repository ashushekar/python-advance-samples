"""
Palindrome Substring Queries
Given a string and several queries on the substrings of the given input string to check
whether the substring is a palindrome or not.

Examples :
Suppose our input string is “abaaabaaaba” and the queries- [0, 10], [5, 8], [2, 5], [5, 9]

[0, 10] → Substring is “abaaabaaaba” which is a palindrome.
[5, 8] → Substring is “baaa” which is not a palindrome.
[2, 5] → Substring is “aaab” which is not a palindrome.
[5, 9] → Substring is “baaab” which is a palindrome.
"""


def ispalindrome(string, query):
    substring = string[query[0]: query[1] + 1]
    if substring == substring[::-1]:
        print("Substring is {} which is a palindrome".format(substring))
    else:
        print("Substring is {} which is not a palindrome".format(substring))


str = "abaaabaaaba"
ispalindrome(str, [0, 10])
ispalindrome(str, [5, 8])
ispalindrome(str, [2, 5])
ispalindrome(str, [5, 9])
