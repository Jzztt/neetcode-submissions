class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_hash = {}
        for index, n in enumerate(numbers):
            my_target= target- n
            if my_target not in my_hash:
                my_hash[n] = index
            else:
                return [my_hash[my_target]+1,index+1]

        