class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res=[]

        for i in range(len(arr),1,-1):
            max_index=arr.index(max(arr[:i]))

            if max_index!=i-1:
                if max_index!=0:
                    arr[:max_index+1]=reversed(arr[:max_index+1])
                    res.append(max_index+1)
                arr[:i]=reversed(arr[:i])
                res.append(i)
        return res


        