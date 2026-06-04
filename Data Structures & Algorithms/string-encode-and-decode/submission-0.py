class Solution:

    def encode(self, strs: List[str]) -> str:
        my_encode = ""
        for word  in strs:
            my_encode+= str(len(word)) + '#' + word 
        return my_encode

    def decode(self, s: str) -> List[str]:
        result =[]
        i = 0
        while i <len(s):
            j=i
            while s[j] != "#":
                j+=1
            word_length= int(s[i:j])
            word = s[j+1:j+1+word_length]
            result.append(word)
            i = j + 1 + word_length
        return result
        

       
        

            
            
            
            

