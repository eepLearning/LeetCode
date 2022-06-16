class Solution:
    def search(self, nums, target):
        answer = -1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return answer
        
        