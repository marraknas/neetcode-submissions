class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = set(nums)
        result = 0
        for num in numMap:
            if num - 1 not in numMap:
                temp = 1
                while num + temp in numMap:
                    temp += 1
                result = max(result, temp)
        return result
            
                