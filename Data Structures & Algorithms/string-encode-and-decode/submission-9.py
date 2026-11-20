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
        print(s)
        result = []
        strs = s.split("-")
        print(strs)

        for string in strs:
            if string == "%":
                result.append("")
                continue
            print(string)
            word = ""
            letters = string.split(".")
            print(letters)
            for letter in letters:
                if letter:
                    word += chr(int(letter))
            if word:
                result.append(word)

        return result

        