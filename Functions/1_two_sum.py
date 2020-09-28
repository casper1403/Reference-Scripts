
"""
Script which takes a list of integers as an input and outputs a list
if indexes which sum up to a given value
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = []
        indexes = []
        for item in nums:
            if item < target:
                sums.append(item)
                indexes.append(nums.index(item))
            if sum(sums) == target:
                return indexes
