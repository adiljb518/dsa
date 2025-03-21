class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        store={}
        for i,a in enumerate(numbers):
            complement=target-a
            if complement in store:
                return [store[complement]+1,i+1]
            else:
                store[a]=i
        