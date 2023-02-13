# Problem
# Given a string s, your task is to reverse the words of s.
# Constraints:
#   length of s <= 10^5
import unittest


def reverse_words(s) -> str:
    """
    Args:
     s(str)
    Returns:
     str
    """

    word = ""
    reverse_of_words = ""
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            word = s[i] + word
        else:
            if len(word) > 0:
                reverse_of_words = reverse_of_words + word
                word = ""
            reverse_of_words = reverse_of_words + s[i]

    if len(word) > 0:
        reverse_of_words = reverse_of_words + word
    return reverse_of_words


class Test(unittest.TestCase):

    # Example 1:
    # Input: "best technical interview prep courses"
    # Output: "courses prep interview technical best"
    def test_example1(self):
        result = reverse_words("best technical interview prep courses")
        self.assertEqual("courses prep interview technical best", result, "Example 1")

    # Example 2:
    # Input: "best  word"
    # Output: "word  best"
    def test_example2(self):
        result = reverse_words("best  word")
        self.assertEqual("word  best", result, "Example 2")

    # Example 3:
    # Input: "word"
    # Output: "word"
    def test_example3(self):
        result = reverse_words("word")
        self.assertEqual("word", result, "Example 3")

    # Example 4:
    # Input: ""
    # Output: ""
    def test_example4(self):
        result = reverse_words("")
        self.assertEqual("", result, "Example 4")
