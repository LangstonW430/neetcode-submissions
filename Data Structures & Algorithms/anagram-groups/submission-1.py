class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for string in strs:
            counter = [0] * 26

            for l in string:
                counter[ord(l) - ord('a')] += 1
            
            key = tuple(counter)

            if not key in groups:
                groups[key] = []

            groups[key].append(string)
        
        return list(groups.values())

                
            
        