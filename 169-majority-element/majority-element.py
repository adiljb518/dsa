class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # n=len(nums)
        # return nums[n//2]
##Sol2
        # candidate = None
        # count = 0
        # for i in range(len(nums)):
        #     if count == 0:
        #         candidate = nums[i]
        #         count+=1
        #     elif nums[i] == candidate:
        #         count+=1
        #     else:
        #         count-=1
        # cand = candidate

        # freq = 0
        # for j in nums:
        #     if j == cand:
        #         freq+=1
        # if freq >= len(nums)//2:
        #     return cand                    
        candidate = None
        count=0
        for i in range(len(nums)):
            if count==0:
                candidate=nums[i]
                count+=1
            elif candidate==nums[i]:
                count+=1
            else:
                count-=1

        # temp=candidate
        cont=0
        for i in nums:
            cont+=1
        if cont> len(nums)//2:
            return candidate
    
