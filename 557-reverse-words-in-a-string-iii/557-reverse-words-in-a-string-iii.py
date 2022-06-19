#Two pointers


class Solution:
    '''try1 : 152ms/14.6mb (10%)
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
        '''
    #try2 : 62ms/14.6mb (50%)
    #아씨 고민안하고 푸는게 훨씬 빠르네
    def reverseWords(self, s: str) -> str:
        return ' '.join([ss[::-1] for ss in s.split(" ")])

                
            
        
        
        