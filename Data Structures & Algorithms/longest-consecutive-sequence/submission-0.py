class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        output = [0]

        for x in s:
            if x - 1 not in s:              # x is the start of a run
                total = 1
                while x + total in s:       # keep checking the next value
                    total += 1
                output.append(total)

        return max(output)