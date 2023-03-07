# Time Complexity :O(n^n)
# Space Complexity :O(n!)
# Did this code successfully run on Leetcode :Yes       
# Any problem you faced while coding this :No


from collections import deque
class Solution(object):
    def removeInvalidParentheses(self, s):
        def isValid(st):
            count=0
            for i in st:
                if(i =='('):
                    count+=1
                elif(i==')'):
                    count-=1
                if(count<0):
                    return False
            return(count==0)
        
        result=[]
        hashset=set()
        q=deque()
        q.append(str(s))
        print(q)
        while(q):
            curr=q.popleft()
            for i in range(len(curr)):
                if(result==[]and (curr[i]=='('or curr[i]==')')):
                    if((curr[0:i]+curr[i+1:]) not in hashset):
                        print(curr[0:i]+curr[i+1:])
                        q.append(curr[0:i]+curr[i+1:])
                        hashset.add(curr[0:i]+curr[i+1:])
                        

            if(isValid(curr)):
                result.append(curr)
                
        if(result==[]):
            return([""])
        return(result)

        
        