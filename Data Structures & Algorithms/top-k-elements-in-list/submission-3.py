from collections import Counter
from random import randint

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = list(count.items())
        n = len(arr)

        def partition(left, right, pivot_idx):
            pivot_freq = arr[pivot_idx][1]
            # Swap
            arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
            prev = left
            for i in range(left, right):
                if arr[i][1] < pivot_freq:
                    arr[prev], arr[i] = arr[i], arr[prev]
                    prev += 1
            arr[right], arr[prev] = arr[prev], arr[right]
            return prev

        def quickselect(left, right, target):
            while left < right:
                pivot_idx = randint(left, right)
                pi = partition(left, right, pivot_idx)
                if pi == target:
                    return
                elif pi > target:
                    right = pi - 1
                else:
                    left = pi + 1
        
        quickselect(0, n - 1, n - k)
        return [num for num, freq in arr[n - k:]]
             


