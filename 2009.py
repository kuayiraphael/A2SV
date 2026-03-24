class Solution:
    def minOperations(self, nums: List[int]) -> int:
        unique_nums = sorted(set(nums))
        left = 0
        n = len(nums)
        ans = n

        for right in range(len(unique_nums)):
            while left<len(unique_nums) and unique_nums[left]<unique_nums[right]+n:
                left +=1
            length = left - right
            ans = min(ans,n-length)

        return ans


