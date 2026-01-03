class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums) 
        left = [1] * size
        right = [1] * size
        
        for i in range(1, size):
            left[i] = nums[i - 1] * left[i - 1]

        for j in range(size - 2, -1, -1):
            right[j] = nums[j + 1] * right[j+1]

        result = []
        for i in range(size):
            result.append(left[i] * right[i])

        return result