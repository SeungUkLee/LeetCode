class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_people = sorted(people, key=lambda p: (-p[0], p[1]))
        q = []
        
        for p in sorted_people:
            q.insert(p[1], p)
        
        return q

