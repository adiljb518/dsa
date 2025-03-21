class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # nums.sort()
        # n = len(nums)
        # if target > nums[n-1]:
        #     sum = 0
        #     for i in range(n-1,n-4,-1):
        #         sum = sum + nums[i]
        # elif target < nums[0]:
        #     sum = nums[0]+nums[1]+nums[2]
        # else:
        #     for i in range(n-2):
        #         j,k = i+1, n-1
        #         sum = nums[i]+nums[j]+nums[k]
        #         while j < k:
        #             if sum > target:
        #                 k-=1
        #             elif sum < target:
        #                 j+=1
        #             else:
        #                 return sum
        # return sum
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        # if target > nums[n-1]:
        #     closest_sum = 0
        #     for i in range(n-1,n-4,-1):
        #         closest_sum = closest_sum + nums[i]
        # elif target < nums[0]:
        #     closest_sum = nums[0]+nums[1]+nums[2]
        # else:
        for i in range(n-2):
            j,k = i+1, n-1
            while j < k:
                current_sum = nums[i]+nums[j]+nums[k]
                if abs(current_sum-target)<abs(closest_sum-target):
                    closest_sum = current_sum
                if current_sum > target:
                    k-=1
                elif current_sum < target:
                    j+=1
                else:
                    return current_sum
        return closest_sum