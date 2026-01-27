class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size = len(nums)
        appeared = {}
        values = []
        for num in nums:
            if num not in appeared:
                appeared[num] = 1
            else:
                 appeared[num] += 1

        for num, freq in appeared.items():
            if freq > ( size / 3):
                values.append(num)
                
        return values