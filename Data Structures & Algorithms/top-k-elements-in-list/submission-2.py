class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        vals = sorted(counter.items(), reverse=True, key=lambda x:x[1])
        sol = []
        for i in range(k):
            sol.append(vals[i][0])
        return sol

        
