# Problem:
#   Given a list of votes, containing names of candidates in an election,
#       find which candidate received maximum number of votes.
#       If two or more candidate got the same number of votes, return the lexicographically smaller name.
# Constraints:
#   length of votes <= 10^5
#   length of votes[i] <= 10^5
#   number of characters in all votes[i] combined <= 10^5
import unittest


def find_winner(votes):
    """
    Args:
     votes(list_str)
    Returns:
     str
    """

    if len(votes) == 0:
        return ""

    popular_candidate = votes[0]
    max_votes = 1
    candidates_by_votes = {}

    for candidate in votes:
        if candidate in candidates_by_votes:
            candidates_by_votes[candidate] = candidates_by_votes[candidate] + 1
        else:
            candidates_by_votes[candidate] = 1

        if candidates_by_votes[candidate] > max_votes:
            popular_candidate = candidate
            max_votes = candidates_by_votes[candidate]
        elif candidates_by_votes[candidate] == max_votes and candidate < popular_candidate:
            popular_candidate = candidate

    return popular_candidate


class Test(unittest.TestCase):

    # Example 1:
    #   Input: ["sam", "john", "jamie", "sam"]
    #   Output: "sam"
    def test_example1(self):
        result = find_winner(["sam", "john", "jamie", "sam"])
        self.assertEqual("sam", result, "Example 1")

    # Example 2:
    #   Input: ["sam", "john", "jamie", "sam", "john"]
    #   Output: "john"
    def test_example2(self):
        result = find_winner(["sam", "john", "jamie", "sam", "john"])
        self.assertEqual("john", result, "Example 2")

    # Example 3:
    #   Input: ["sam", "john", "jamie", "sam", "john", "sam"]
    #   Output: "sam"
    def test_example3(self):
        result = find_winner(["sam", "john", "jamie", "sam", "john", "sam"])
        self.assertEqual("sam", result, "Example 3")

    # Example 4:
    #   Input: []
    #   Output: ""
    def test_example4(self):
        result = find_winner([])
        self.assertEqual("", result, "Example 4")
