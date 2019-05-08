from typing import List


def missing_number(nums: List[int]) -> int:
    """Given an array containing n distinct numbers
    taken from 0, 1, 2, ..., n, find the one that
    is missing from the array.

    From `leetcode <https://leetcode.com/problems/missing-number/>`

    :param nums: {List[int]} 0, 1, 2, ..., n
    :return: {int} missing number in array
    """
    nums.sort()

    num = nums[0]
    length = len(nums)

    if length == 1:
        return num - 1 if num > 0 else num + 1

    if 0 not in nums:
        return 0

    for i in range(1, length):
        num = nums[i - 1] + 1
        if nums[i] != num:
            break
        num += 1

    return num
