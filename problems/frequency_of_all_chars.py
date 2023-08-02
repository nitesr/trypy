# Problem:
#   Find frequency of all lowercase English letters in a given string.
#
# Example:
#   Input: s = "crabcactus"
#   Output: [2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
#   Explanation:
#       In the output, we have:
#           2 at the 0th index denoting the frequency of 'a' (0th character of the English alphabet)
#           1 at the 1st index denoting the frequency of 'b' (1st character of the English alphabet)
#           3 at the 2nd index denoting the frequency of 'c' (2nd character of the English alphabet)
#           and so on.
#
# Constraints:
#   1 <= length of the input string <= 10^5
#   The input string contains lowercase English letters only.
import unittest


def get_frequency_of_characters(s):
    """
    Args:
     s(str)
    Returns:
     list_int32
    """
    # Solution:
    #   maintain the lowercase alpha index & keep incrementing when you find the character
    #   return the index itself.
    #
    # Write your code here.

    alpha_index = [0 for i in range(26)]
    a_int = ord('a')
    for c in s:
        c_int = ord(c) - a_int
        alpha_index[c_int] = alpha_index[c_int] + 1

    return alpha_index


class Testcase(unittest.TestCase):
    def test_example(self):
        s = "crabcactus"
        output = get_frequency_of_characters(s)
        self.assertEqual([2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                         output, "example")

    def test_single_char(self):
        s = "a"
        output = get_frequency_of_characters(s)
        self.assertEqual([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         output, "singleChar")

    def test_multi_single_char(self):
        s = "abcxyz"
        output = get_frequency_of_characters(s)
        self.assertEqual([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                         output, "multiSingleChar")

    def test_single_repeated_char(self):
        s = "ddddddd"
        output = get_frequency_of_characters(s)
        self.assertEqual([0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         output, "single_repeated_char")