from typing import List


def intersect(nums1: List[int],
              nums2: List[int]) -> List[int]:
    """Given two arrays of integers, write a function to compute their intersection.

    From `leetcode <https://leetcode.com/problems/intersection-of-two-arrays-ii/>`

    Note:
        - Each element in the result should appear as many times as it shows in both arrays.
        - The result can be in any order.

    :param nums1: {List[int]}
    :param nums2: {List[int]}
    :return: {List[int]} intersection of two arrays
    """
    output = []

    for n in nums1:
        if n in nums2:
            output.append(n)
            nums2.remove(n)

    return output
