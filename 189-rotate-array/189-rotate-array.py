#Two Pointers
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2 = []
        start = (len(nums) -  k) % len(nums)

        for i in range(start,len(nums)):
            nums2.append(nums[i])
        if start !=0: 
            for i in range(start):
                nums2.append(nums[i])
        #nums = nums2
        for i in range(len(nums)):
            nums[i] = nums2[i]
                
        
