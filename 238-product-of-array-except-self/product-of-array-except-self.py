class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #https://www.youtube.com/watch?v=PjZxg3A_4-Y
        n = len(nums)
        left_product = [1]*n
        for i in range(1,n):
            left_product[i] = left_product[i-1]*nums[i-1]
        right_product = 1
        for i in reversed(range(n-1)):
            right_product *= nums[i+1]
            left_product[i] *= right_product
        return left_product
        