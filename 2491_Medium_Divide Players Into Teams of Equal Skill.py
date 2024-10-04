class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill = sorted(skill)
        left = 0
        right = n - 1
        pivot = skill[left] + skill[right]
        chemistry = skill[left] * skill[right]
        left += 1
        right -= 1
        while left < right:
            if skill[left] + skill[right] == pivot:
                chemistry += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1

        return chemistry
