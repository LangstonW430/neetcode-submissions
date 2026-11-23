class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        temp = 1
        for i, num in enumerate(nums):
            prefix[i] = temp
            temp *= num
        
        temp = 1
        for i, num in reversed(list(enumerate(nums))):
            suffix[i] = temp
            temp *= num
        
        solution = [suffix[n] * prefix[n] for n in range(len(nums))]
        return solution