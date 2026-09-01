class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Intuition: Check if target - nums[i] is in the hashmap
        # So build hashmap first
        hashMap = {} # number -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[num] = i
        return []
            
