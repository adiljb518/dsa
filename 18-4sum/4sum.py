class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        k = 4, start = 0, target = 0.

Recursive Case (k = 4)
First Iteration (i = 0):

nums[0] = -2.

quad = [-2].

Recursive call: kSum(3, 1, 2) (since target - (-2) = 2).

Second Call to kSum (k = 3, start = 1, target = 2):

First Iteration (i = 1):

nums[1] = -1.

quad = [-2, -1].

Recursive call: kSum(2, 2, 3) (since target - (-1) = 3).

Third Call to kSum (k = 2, start = 2, target = 3):

Initialize two pointers: l = 2, r = 5.

First Iteration:

nums[2] + nums[5] = 0 + 2 = 2 < 3 → l += 1 (l = 3).

Second Iteration:

nums[3] + nums[5] = 0 + 2 = 2 < 3 → l += 1 (l = 4).

Third Iteration:

nums[4] + nums[5] = 1 + 2 = 3 == 3 → Add [-2, -1, 1, 2] to res.

l += 1 (l = 5).

Skip duplicates: l = 5 (no duplicates here).

Back to Second Call (k = 3):

quad = [-2, -1].

quad.pop() → quad = [-2].

Second Iteration (i = 2):

nums[2] = 0.

quad = [-2, 0].

Recursive call: kSum(2, 3, 2) (since target - 0 = 2).

Fourth Call to kSum (k = 2, start = 3, target = 2):

Initialize two pointers: l = 3, r = 5.

First Iteration:

nums[3] + nums[5] = 0 + 2 = 2 == 2 → Add [-2, 0, 0, 2] to res.

l += 1 (l = 4).

Skip duplicates: l = 4 (no duplicates here).

Back to Second Call (k = 3):

quad = [-2, 0].

quad.pop() → quad = [-2].

Third Iteration (i = 3):

nums[3] = 0 (duplicate of previous) → Skip.

Back to First Call (k = 4):

quad = [-2].

quad.pop() → quad = [].

Second Iteration (i = 1):

nums[1] = -1.

quad = [-1].

Recursive call: kSum(3, 2, 1) (since target - (-1) = 1).

Fifth Call to kSum (k = 3, start = 2, target = 1):

First Iteration (i = 2):

nums[2] = 0.

quad = [-1, 0].

Recursive call: kSum(2, 3, 1) (since target - 0 = 1).

Sixth Call to kSum (k = 2, start = 3, target = 1):

Initialize two pointers: l = 3, r = 5.

First Iteration:

nums[3] + nums[5] = 0 + 2 = 2 > 1 → r -= 1 (r = 4).

Second Iteration:

nums[3] + nums[4] = 0 + 1 = 1 == 1 → Add [-1, 0, 0, 1] to res.

l += 1 (l = 4).

Skip duplicates: l = 4 (no duplicates here).

Back to Fifth Call (k = 3):

quad = [-1, 0].

quad.pop() → quad = [-1].

Second Iteration (i = 3):

nums[3] = 0 (duplicate of previous) → Skip.

Back to First Call (k = 4):

quad = [-1].

quad.pop() → quad = [].

Third Iteration (i = 2):

nums[2] = 0.

quad = [0].

Recursive call: kSum(3, 3, 0) (since target - 0 = 0).

Seventh Call to kSum (k = 3, start = 3, target = 0):

First Iteration (i = 3):

nums[3] = 0.

quad = [0, 0].

Recursive call: kSum(2, 4, 0) (since target - 0 = 0).

Eighth Call to kSum (k = 2, start = 4, target = 0):

Initialize two pointers: l = 4, r = 5.

First Iteration:

nums[4] + nums[5] = 1 + 2 = 3 > 0 → r -= 1 (r = 4).

Second Iteration:

l = 4, r = 4 → Exit loop.

Back to Seventh Call (k = 3):

quad = [0, 0].

quad.pop() → quad = [0].

Second Iteration (i = 4):

nums[4] = 1.

quad = [0, 1].

Recursive call: kSum(2, 5, -1) (since target - 1 = -1).

Ninth Call to kSum (k = 2, start = 5, target = -1):

Initialize two pointers: l = 5, r = 5.

Exit loop immediately since l is not less than r.

Back to Seventh Call (k = 3):

quad = [0, 1].

quad.pop() → quad = [0].

Third Iteration (i = 5):

nums[5] = 2.

quad = [0, 2].

Recursive call: kSum(2, 6, -2) (since target - 2 = -2).

Tenth Call to kSum (k = 2, start = 6, target = -2):

Exit immediately since start is beyond the list length.

Back to Seventh Call (k = 3):

quad = [0, 2].

quad.pop() → quad = [0].

Back to First Call (k = 4):

quad = [0].

quad.pop() → quad = [].

Fourth Iteration (i = 3):

nums[3] = 0 (duplicate of previous) → Skip.

Back to First Call (k = 4):

quad = [].

Fifth Iteration (i = 4):

nums[4] = 1.

quad = [1].

Recursive call: kSum(3, 5, -1) (since target - 1 = -1).

Eleventh Call to kSum (k = 3, start = 5, target = -1):

Exit immediately since start is beyond the list length.

Back to First Call (k = 4):

quad = [1].

quad.pop() → quad = [].

Sixth Iteration (i = 5):

nums[5] = 2.

quad = [2].

Recursive call: kSum(3, 6, -2) (since target - 2 = -2).

Twelfth Call to kSum (k = 3, start = 6, target = -2):

Exit immediately since start is beyond the list length.

Back to First Call (k = 4):

quad = [2].

quad.pop() → quad = [].

Final Result
After all iterations, res contains the following unique quadruplets:

python
Copy
[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        '''

        ##Brute Force
        # nums.sort()
        # store=[]
        # n=len(nums)
        # # print(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         k,l = j+1,n-1
        #         # print(i,j,k,l)
        #         while k<l:
        #             # print(k,l)
        #             sum=nums[i]+nums[j]+nums[k]+nums[l]
        #             # print('sum=',sum)
        #             if sum < target:
        #                 k+=1
        #                 if nums[k] == nums[k-1]:
        #                     # print('found same')   
        #                     k+=1
        #                     continue
        #             elif sum > target:
        #                 l-=1
        #             else:
        #                 # print('target found')
        #                 store.append([nums[i],nums[j],nums[k],nums[l]])
        #                 k+=1
        # return store
        nums.sort()
        res,quad = [],[]
        def kSum(k,start,target):
            if k!=2:
                for i in range(start, len(nums)-k+1):
                    if i > start and nums[i]==nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1,i+1,target-nums[i])
                    quad.pop()
                return
            l,r = start, len(nums)-1
            while l<r:
                if nums[l]+nums[r] < target:
                    l+=1
                elif nums[l]+nums[r] > target:
                    r-=1
                else:
                    res.append(quad + [nums[l],nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        kSum(4,0,target)
        return res