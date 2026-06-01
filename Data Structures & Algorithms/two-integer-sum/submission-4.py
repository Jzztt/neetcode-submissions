class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        
        for i,item in enumerate(nums):
            diff = target-item
            if i > 0 and diff in my_dict:
                return [my_dict[diff],i]
            my_dict[item] = i
        return []

        