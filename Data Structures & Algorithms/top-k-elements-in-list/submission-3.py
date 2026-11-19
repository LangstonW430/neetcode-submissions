class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            if num in counter:
                counter[num] = counter[num] + 1
            else:
                counter[num] = 1
        
        sort = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        result = [sort[n][0] for n in range(k)]

        return result

        
