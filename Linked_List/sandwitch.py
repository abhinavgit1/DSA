class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cn = Counter(students)
        res = len(students)
        for s in sandwiches:
            if cn[s]>0:
                res-=1
                cn[s]-=1
            else:
                return res
        return res