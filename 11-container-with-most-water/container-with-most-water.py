class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        start with left and right pointer. calculate the difference between left and right pointer and multiply it with min of left and right.intialise area with zero and when new one is calculated, store the max of these two. increment the side with min height.
        '''
        l,r = 0,len(height)-1
        max_area=0
        while l < r:
            curr_area = (r-l)*min(height[l],height[r])
            if curr_area > max_area:
                max_area = curr_area
            if height[l]<=height[r]:
                l+=1
            # elif height[l]>height[r]:
            else:
                r-=1
        return max_area
        