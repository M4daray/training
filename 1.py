import itertools

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ """
        indices = range(0, len(nums))
        combinations = itertools.combinations(indices, 2)
        solution = []
        for pair in combinations:
            result: int = nums[pair[0]] + nums[pair[1]]
            if result == target:
                solution = [pair[0], pair[1]]
                break
        return solution
        