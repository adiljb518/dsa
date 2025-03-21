class Solution:
    def isPalindrome(self, s: str) -> bool:
        # t=""
        # for i in s.lower():
        #     if i.isalnum():
        #         t=t+i
        # r=t[::-1]
        # return True if r==t else False

        # t=s.lower()
        # l,r = 0,len(t)-1
        # if len(s.strip())==0:
        #     return True
        # for i in range(len(t)):
        #     # print(i)
        #     if t[l].isalnum() and t[r].isalnum():
        #         if t[l]==t[r]:
        #             # print(t[l],t[r])
        #             if i == len(t)-1:
        #                 return True
        #             l+=1
        #             r-=1   
        #         else:
        #             return False
        #     elif not t[l].isalnum():
        #         l+=1
        #     elif not t[r].isalnum():
        #         r-=1
        #     else:
        #         return False
        n = len(s) #length of the string
        L = 0 #left starting point
        R = n - 1 #right starting point

        while L < R : #left is less than right
            if not s[L].isalnum(): # if character is not alphanumeric, we increment and continue
                L += 1
                continue
            
            if not s[R].isalnum(): # if character is not alphanumeric, we decrement and continue
                R -= 1
                continue
            
            if s[L].lower() != s[R].lower(): # meaning they are different characters. so, we return false
                return False
            
            L += 1 #meaning everything is going well, we increment
            R -= 1 #going well so we decrement
        
        return True
        
