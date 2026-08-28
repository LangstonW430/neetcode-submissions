class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return chr(257)
        result = ""
        for string in strs:
            for char in string:
                result = result + str(ord(char)) + "."
            result = result + "-"
        
        return result[:-1]

    def decode(self, s: str) -> List[str]:
        if s == chr(257):
            return []
        words = s.split("-")
        result = []

        for word in words:
            res = ""
            chars = word.split(".")
            for char in chars:
                if char:
                    res = res + chr(int(char))

            result.append(res)
        
        return result