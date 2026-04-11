class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_queue = deque()
        results = []

        for right in range(len(nums)):
            while max_queue and nums[max_queue[-1]]<nums[right]:
                max_queue.pop()
            
            while max_queue and right- max_queue[0]>k-1:
                max_queue.popleft()
            
            max_queue.append(right)

            if right>=k-1:
                results.append(nums[max_queue[0]])

        return results

            


            