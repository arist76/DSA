class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        
        for v, e in  enumerate(points):
            dis = math.sqrt(
                e[0]**2 +
                e[1]**2
            )
        
            distance.append((v, dis))
            
        sorted_distance = sorted(distance, key=lambda x:x[1])
        
        shortest = []
        for each in range(k):
            shortest.append(points[sorted_distance[each][0]])
            
        return shortest
            
            
        
 