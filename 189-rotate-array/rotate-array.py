class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if len(nums)==1:
        #     return nums
        # else:
        #     if k > len(nums):
        #         k = k % len(nums)
        #     l=len(nums)-k
        #     for i in range(k):
        #         temp = nums[i]
        #         nums[i] = nums[l]
        #         for j in range(l,i,-1):
        #             if j == i+1:
        #                 nums[j]=temp
        #             else:
        #                 nums[j]=nums[j-1]
        #         l+=1
        # 
        # nums1=[]
        # nums2=[]
        # if k == len(nums):
        #     return nums
        # else:
        #     if k > len(nums):
        #         k = k % len(nums)
        #     nums1[:] = nums[0:len(nums)-k]
        #     nums2[:] = nums[len(nums)-k:]
        #     nums = nums1+nums2
        #
        for i in range(k):
             nums.insert(0,nums.pop())
