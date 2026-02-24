class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total=skill[0]+skill[-1]
        chemistry_sum=0

        for i in range(len(skill)//2):
            if skill[i]+skill[-i-1]!=total:
                return -1
            else:
                chemistry_sum+=skill[i]*skill[-i-1]

        return chemistry_sum
        
