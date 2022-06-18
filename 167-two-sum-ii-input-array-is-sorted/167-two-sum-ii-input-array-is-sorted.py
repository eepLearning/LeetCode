#Topic: Binary Search, Two Pointers
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        table = dict()
        for idx,n in enumerate(numbers):
    
            if n not in table:
                table[(target-n)] = idx
            else:
                return table[n]+1, idx+1

                
        
        