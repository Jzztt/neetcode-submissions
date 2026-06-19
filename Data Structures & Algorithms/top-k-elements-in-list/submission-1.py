class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_hash={}
        for num in nums:
           my_hash[num] = my_hash.get(num,0) + 1
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in my_hash.items():
            bucket[freq].append(num)
        print(bucket)

        result = []
        for freq in range(len(bucket)-1, 0, -1):
            for num in bucket[freq]:
                result.append(num)

                if len(result) == k:
                    return result



        