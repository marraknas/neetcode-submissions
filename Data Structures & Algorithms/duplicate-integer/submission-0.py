class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                # update the count
                # actually can just return true
                return True
            else:
                hashMap[num] = hashMap.get(num, 0) + 1
        return False
        