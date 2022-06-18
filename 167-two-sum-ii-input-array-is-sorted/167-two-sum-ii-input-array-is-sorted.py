#Topic: Binary Search, Two Pointers
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        hash 풀이법
        시간 복잡도: n
        공간복잡도: n
        
        table = dict()
        for idx,n in enumerate(numbers):
    
            if n not in table:
                table[(target-n)] = idx
            else:
                return table[n]+1, idx+1
        216 ms / 15 MB
        '''
            
        start = 0
        end = len(numbers) - 1
        
        while start <= end:
            s = numbers[start] + numbers[end]
            if s == target:
                return start + 1, end + 1
            elif s < target:
                start  += 1
            else:
                end -=1 
            
