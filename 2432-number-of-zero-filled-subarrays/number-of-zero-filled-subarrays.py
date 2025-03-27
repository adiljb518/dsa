class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        local_count = 0
        global_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                local_count += 1
                global_count = global_count + local_count
            else:
                local_count = 0
        return global_count
        # return local_count
            