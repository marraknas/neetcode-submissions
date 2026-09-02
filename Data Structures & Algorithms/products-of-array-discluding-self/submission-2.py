class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = []
        prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count.append([0, i])
            else:
                prod *= nums[i]
        print(zero_count, prod)

        # one pass done to find number of zeroes
        # if >1 zero: all 0
        if len(zero_count) > 1:
            return [0] * len(nums)
        elif len(zero_count) == 1:
            index = zero_count[0][1]
            arr = [0] * len(nums)
            arr[index] = prod
            return arr
        else:
            for i in range(len(nums)):
                nums[i] = prod // nums[i]
            return nums
        return [] # not reachable
            
               