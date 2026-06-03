class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict={}
        for index,value in enumerate(nums):
            if value in my_dict:
                my_dict[value] +=1
            else:
                my_dict[value] = 1
        sorted_items =sorted(my_dict.items(), key=lambda item: item[1])
        result = []
        for key, value in sorted_items[-k:]:
            result.append(key)

        return result


    


        