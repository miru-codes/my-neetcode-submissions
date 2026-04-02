class Solution:
    def findMaxConsecutiveOnes(self, num: List[int]) -> int:
        t=0
        m=0
        for i in num:
            if i==1:
                t+=1
            else:
                if m<t:
                    m=t
                t=0
        if m<t:
            m=t
        return m