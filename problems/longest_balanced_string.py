# Problem:
#   Find the longest balanced substring in a given string of letters.
#   A string is balanced if every letter in the string appears
#       in both uppercase and lowercase.
# Example 1:
#   Input: "GOogleLEns"
#   Output: "GOogleLE"
# Example 2;
#   Input: "aPPle"
#   Ouptut: ""
# Constratints:
#   1 <= size of the input string <= 10^5
# Solution:
#   BruteForce:
#       we know we have n^2 substrings, we can generate them and
#           check if a given substring is balanced from length n to 0
#       to check if a given substring is balanced, we can traverse
#           and check if other case is already visted using an index/map
#   Optimization:
#       we can split the string at the characters which are not balanced and
#           recursively validate if the string is balanced using bruteforce
import unittest


def longest_balanced_substring(char_list, start_index, end_index):
    if end_index <= start_index:
        return str("")

    uc_start_int = ord('A')
    uc_end_int = ord('Z')
    lc_start_int = ord('a')
    lc_end_int = ord('z')
    case_diff = lc_start_int - uc_start_int
    alpha_index = [False for i in range(0, lc_end_int - uc_start_int + 1)]

    for i in range(start_index, end_index + 1):
        char_int = ord(char_list[i])
        alpha_index[char_int - uc_start_int] = True

    unbalanced_pos = []
    for i in range(start_index, end_index + 1):
        char_int = ord(char_list[i])

        other_case_char_int = char_int + case_diff
        if other_case_char_int > lc_end_int:
            other_case_char_int = char_int - case_diff

        if not alpha_index[other_case_char_int - uc_start_int]:
            unbalanced_pos.append(i)

    if unbalanced_pos:
        unbalanced_pos.append(end_index + 1)

    longest_balanced_string = ""
    string_start = start_index
    for i in unbalanced_pos:
        string_end = i - 1
        # print("checking substring", "".join(char_list[string_start:string_end+1]))
        balanced_string = longest_balanced_substring(char_list, string_start, string_end)
        string_start = i + 1
        if len(balanced_string) > len(longest_balanced_string):
            longest_balanced_string = balanced_string

    return longest_balanced_string if unbalanced_pos else "".join(char_list[start_index:end_index + 1])


def find_longest_balanced_substring(s):
    """
    Args:
     s(str)
    Returns:
     str
    """
    # Write your code here.
    char_list = [c for c in s]
    return longest_balanced_substring(char_list, 0, len(s) - 1)


class Testcase(unittest.TestCase):
    def test_example1(self):
        input = "GOogleLEns"
        expected = "GOogleLE"
        actual = find_longest_balanced_substring(input)
        self.assertEqual(expected, actual, "example1")

    def test_example2(self):
        input = "aPPle"
        expected = ""
        actual = find_longest_balanced_substring(input)
        self.assertEqual(expected, actual, "example2")

    def test_mid(self):
        input = "aXPpPxle"
        expected = "XPpPx"
        actual = find_longest_balanced_substring(input)
        self.assertEqual(expected, actual, "mid")
