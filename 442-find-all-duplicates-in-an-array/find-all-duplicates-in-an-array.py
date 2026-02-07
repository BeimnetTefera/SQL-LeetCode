class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()

        left_ptr = 0
        right_ptr = 1
        result = []

        while right_ptr < len(nums):
            
            if nums[left_ptr] == nums[right_ptr]:
                result.append(nums[left_ptr])

            left_ptr += 1
            right_ptr += 1

        return result