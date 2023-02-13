# https://leetcode.com/problems/bulb-switcher/
# There are n bulbs that are initially off. You first turn on all the bulbs,
#   then you turn off every second bulb.
# On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on).
#   For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
# Return the number of bulbs that are on after n rounds.
#
# Constraints:
# 0 <= n <= 10^9

import math


def num_bulbs_on(n) -> int:
    # 1-st bulb is on
    # 2-nd bulb is off (1 for on & 2 for off)
    # i-th bulb is on if it is toggled odd number of times
    #   that should be equal to number of factors (e.g. i=10 will be toggled for 1, 2, 5, 10)
    #   and perfect squares have odd number of factors (e.g i=49 will be toggled for 1, 7, 49)
    return int(math.sqrt(n))

# Example 1:
#   Input: n = 3
#   Output: 1
# Example 2:
#   Input: n = 0
#   Output: 0
# Example 3:
#   Input: n = 1
#   Output: 1
