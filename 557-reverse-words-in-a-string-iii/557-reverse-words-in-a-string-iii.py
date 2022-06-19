#Two pointers


class Solution:
    
    def reverseWords(self, s: str) -> str:
        answer = []
        start = 0
        zero = 0
        
        for idx,ss in enumerate(s):
            if (ss == " "):
                answer.append(''.join(s[start:zero][::-1]))
                start = zero + 1 
            elif (idx == len(s) -1):
                answer.append(''.join(s[start:idx+1][::-1]))
                
            zero = zero + 1
        return ' '.join(answer)
                
            
        
        
        