class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        running = 1
        
        for num in nums[:-1]:
            running *= num
            left.append(running)

        right = [1]
        running = 1

        for i in range(len(nums) - 1, 0, -1):
            running *= nums[i]
            right.append(running)

        right.reverse()
        result = []

        for i in range(len(nums)):
            result.append(right[i] * left[i])

        return result