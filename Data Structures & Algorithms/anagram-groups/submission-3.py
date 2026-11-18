class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = dict()

        for word in strs:
            
            letters = dict()

            for l in word:
                if l in letters:
                    letters[l] = letters[l] + 1
                else:
                    letters[l] = 1

            letters = tuple(sorted(letters.items()))

            if letters in result:
                result[letters].append(word)
            else:
                result[letters] = [word]
        
        return list(result.values())

                
            
        