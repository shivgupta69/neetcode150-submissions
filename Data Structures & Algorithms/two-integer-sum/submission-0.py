class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {} # it stores the value and index no.

        for i, n in enumerate(nums): ## using for loop to get the
        ## index no and value.
            diff = target - n  ## the provided target - value
            ## store the diff in hashmap and iterate another value
            if diff in prevMap:
                return [prevMap[diff], i] 
            ## if the difference is already persent in pervmap
            ## it returns the index no of both values .
            prevMap[n] = i ## used to store value and index no in hashmap.