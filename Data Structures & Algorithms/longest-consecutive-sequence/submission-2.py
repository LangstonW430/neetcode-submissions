class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = dict()

        for num in nums:
            if num in seen:
                continue
            prev = num - 1
            follow = num + 1
            if prev in seen and follow in seen:
                new = seen[prev] + seen[follow] + 1
                seen[num - seen[prev]] = new
                seen[num + seen[follow]] = new
                seen[num] = 1
            elif prev in seen:
                new = seen[prev] + 1
                seen[num] = new
                seen[num - seen[prev]] = new
            elif follow in seen:
                new = seen[follow] + 1
                seen[num] = new
                seen[num + seen[follow]] = new
            else:
                seen[num] = 1
            
        if seen:
            return max(list(seen.values()))
        else:
            return 0