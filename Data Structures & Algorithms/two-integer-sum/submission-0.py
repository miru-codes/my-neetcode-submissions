class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rr = []
        for i in range(len(nums)):
            t = target - nums[i]
            if t in nums:
                rr = [i, nums.index(t)]
        rr.sort()
        return rr
        