class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            if not word:
                result += "%-"
                continue
            for letter in word:
                result += str(ord(letter))
                result += "."
            result += "-"
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        strs = s.split("-")

        for string in strs:
            if string == "%":
                result.append("")
                continue
            
            word = ""
            letters = string.split(".")

            for letter in letters:
                if letter:
                    word += chr(int(letter))
            if word:
                result.append(word)

        return result

        