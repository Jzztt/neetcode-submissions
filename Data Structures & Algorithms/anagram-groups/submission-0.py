class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict={}
        for item in strs:
            words= []
            for i,str in enumerate(item):
                if i < len(item):
                    words.append(str)
            words.sort()
            word = "".join(words)
            if word not in my_dict:
                my_dict[word] = []
            my_dict[word].append(item)
        return list(my_dict.values())
       

            
        