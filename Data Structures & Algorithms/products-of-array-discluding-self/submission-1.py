class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        temp = [1] * length
        running = 1
        
        for i, num in enumerate(nums[:-1]):
            running *= num
            temp[i + 1] = running
        
        result = temp.copy()
        temp[-1] = 1
        running = 1

        for i in range(len(nums) - 1, 0, -1):
            running *= nums[i]
            temp[i - 1] = running

        for i in range(len(nums) - 1):
            result[i] = result[i] * temp[i]

        return result