class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = dict()

        for l in s:
            letters[l] = letters.get(l, 0) + 1

        for l in t:
            if letters.get(l, 0) < 1:
                return False
            
            if letters[l] == 1:
                letters.pop(l)
            else:
                letters[l] = letters.get(l, 0) - 1
        return letters == dict()