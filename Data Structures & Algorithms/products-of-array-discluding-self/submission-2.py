class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        running = 1
        
        for i, num in enumerate(nums[:-1]):
            running *= num
            result[i + 1] = running
        
        right = [1] * length
        running = 1

        for i in range(len(nums) - 1, 0, -1):
            running *= nums[i]
            right[i - 1] = running

        for i in range(len(nums) - 1):
            result[i] = result[i] * right[i]

        return result