class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value_processed = set()
        value_processed = set(nums)
        if len(nums) == len(list(value_processed)):
            return False
        else:
            return True        