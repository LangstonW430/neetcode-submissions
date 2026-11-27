class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = set("abcdefghijklmnopqrstuvwxyz1234567890")
        copy = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            first = copy[left]
            second = copy[right]
            
            if first in alphabet and second in alphabet:
                if first != second:
                    return False
                else:
                    left += 1
                    right -= 1
            else:
                if first not in alphabet:
                    left += 1
                if second not in alphabet:
                    right -= 1
            
        return True