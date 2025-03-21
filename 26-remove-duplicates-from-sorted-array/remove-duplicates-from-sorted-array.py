class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=0
        # for j in range(len(nums)):
        #     if nums[j] == nums[i]:
        #         j+=1
        #     else:
        #         i+=1
        #         nums[i]=nums[j]
        # # nums[:]=nums[0:i+1]
        # # del nums[i+1:]
        # # return len(nums)
        # return i+1
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i+=1
                nums[i]=nums[j]    
        # nums[:]=nums[0:i+1]
        # del nums[i+1:]
        # return len(nums)
        return i+1