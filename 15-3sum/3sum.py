class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # store={}
        # for i,a in enumerate(nums):
        #     target = -a
        #     for j in range(i+1,len(nums)-1):
        #         val = target - nums[j]
        #         if val in store:
        #             return [a,nums[j],val]
        #         else:
        #             store[val]

        ##2 Pointers
        nums.sort()
        res=[]
        for i,a in enumerate(nums):
            if a > 0:
                break
            elif i > 0 and a == nums[i-1]:
                continue
            lo,hi=i+1,len(nums)-1
            while lo < hi:
                sum = a + nums[lo] + nums[hi]
                if sum > 0:
                    hi-=1
                elif sum < 0:
                    lo+=1
                else:
                    res.append([a,nums[lo],nums[hi]])
                    lo+=1
                    while nums[lo] == nums[lo-1] and lo < hi:
                        lo+=1
        return res

        ##Brute Force
        # lst=[]
        # for i in range(len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         for k in range(j+1,len(nums)):
        #             # print(i,j,k)
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 res=[nums[i],nums[j],nums[k]]
        #                 # print(i,j,k)
        #                 lst.append(res)
        #                 # print(lst)
        #                 for s in range(len(lst),1,-len(lst)):
        #                     for m in range(s-1,0,-1):
        #                     # print("inloops")
        #                         # if len(lst) > 0:
        #                         # print(s,m)
        #                         # if set.intersection(set(lst[s-1]),set(lst[m-1]))== set(lst[s-1]):
        #                         if (set(lst[s-1]) == set(lst[m-1])):
        #                             # print(s,m)
        #                             # print("found intersection")
        #                             lst.pop(s-1)
        #                             break
        #                             # print(lst)
        # return lst
