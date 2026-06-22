class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for word in s:
            if word.isalnum():
                clean +=word.lower()
        return clean == clean[::-1]
    

        