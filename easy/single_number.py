from typing import List


def single_number(nums: List[int]) -> int or None:
    """Given a non-empty array of integers, every element appears twice except for one. Find that single one.

    From `leetcode <https://leetcode.com/problems/single-number/>`

    Note:
        - Your algorithm should have a linear runtime complexity.
          Could you implement it without using extra memory?

    :param nums:
    :return: {int}
    """
    no_duplicate_list = []

    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)

    return no_duplicate_list.pop()
