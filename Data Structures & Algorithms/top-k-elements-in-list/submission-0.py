class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        key = {}

        for num in nums:
            if num in key:
                key[num] += 1
            else:
                key[num] = 1

        sorted_keys = sorted(key, key=key.get, reverse=True)

        return sorted_keys[:k]
