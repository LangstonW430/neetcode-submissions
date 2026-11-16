class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = dict()
        tCounter = dict()

        for letter in s:
            if letter in sCounter:
                sCounter[letter] = sCounter[letter] + 1
            else:
                sCounter[letter] = 1
        
        for letter in t:
            if letter in tCounter:
                tCounter[letter] = tCounter[letter] + 1
            else:
                tCounter[letter] = 1
        
        return sCounter == tCounter