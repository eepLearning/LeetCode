#Topic: Two Pointers
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2 = list(nums)
        start = 0 
        end = len(nums2) -1 
        
        for i in nums:
            if i != 0:
                nums2[start] = i
                start = start + 1
            else:
                nums2[end] = i
                end = end - 1
            
            
        for i in range(len(nums)):
            nums[i] =nums2[i]