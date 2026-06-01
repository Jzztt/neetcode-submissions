class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_results = set(nums);
        return len(my_results) < len(nums)
        