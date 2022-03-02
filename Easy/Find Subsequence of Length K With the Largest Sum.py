class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        temp = sorted(nums)
        for i in range(len(nums) - k):
            nums.remove(temp[i])
        return nums
