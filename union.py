class Solution:    
    def findUnion(self, a, b):
        # code here
        result=[] 
        for i in a: 
            if i not in result:
                result.append(i)
        for j in b:
            if j not in result:
                result.append(j)
        return result
