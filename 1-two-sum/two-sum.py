class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            val = target-nums[i]
            if val in store:
                return [i,store[val]]
            else:
                store[nums[i]]=i

                