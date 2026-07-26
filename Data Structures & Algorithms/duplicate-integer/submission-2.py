class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        is_set = set()
        for num in nums:
            if num in is_set:
                return True
            is_set.add(num)
        return False
