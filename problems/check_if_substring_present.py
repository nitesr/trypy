# Problem:
#   Given a string s and a substring substring, check if substring is present in s or not.
# Constraints:
#   length of s <= 10^5
#   length of s <= length of substring

import unittest


def check_if_substring_present(s, substring):
    """
    Args:
     s(str)
     substring(str)
    Returns:
     bool
    """

    lo = 0
    i = 0  # points to position on substring
    while lo < len(s):
        if i == len(substring):  # substring matched
            return True
        elif substring[i] == s[lo + i]:  # part of substring matched
            i = i + 1
        else:  # mismatch, so increment the lower index and start comparing again from i=0
            lo = lo + 1
            i = 0

    return i == len(substring)


class Test(unittest.TestCase):
    # Example 1:
    # Input:
    #   "s": "interview kickstart",
    #   "substring": "interview"
    # Output:
    #   True
    def test_example1(self):
        result = check_if_substring_present("interview kickstart", "interview")
        self.assertEqual(True, result, "Example 1")

    # Example 2:
    # Input:
    #   "s": "interview kickstart",
    #   "substring": "internet"
    # Output:
    #   False
    def test_example2(self):
        result = check_if_substring_present("interview kickstart", "internet")
        self.assertEqual(False, result, "Example 2")

    # Example 3:
    # Input:
    #   "s": "aaaaaaaaaaa",
    #   "substring": "a"
    # Output:
    #   True
    def test_example3(self):
        result = check_if_substring_present("aaaaaaaaaaa", "a")
        self.assertEqual(True, result, "Example 3")

    # Example 4:
    # Input:
    #   "s": "abcd",
    #   "substring": "abcd"
    # Output:
    #   True
    def test_example4(self):
        result = check_if_substring_present("abcd", "abcd")
        self.assertEqual(True, result, "Example 4")
