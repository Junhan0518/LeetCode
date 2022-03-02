class Solution:
    def countPoints(self, rings: str) -> int:
        ring ={}
        count = 0
        for i in range(1, len(rings)):
            if i % 2 != 0:
                if rings[i] not in ring.keys():
                    ring[rings[i]] = [rings[i-1]]
                else:
                    if rings[i-1] not in ring[rings[i]]:
                        ring[rings[i]].append(rings[i-1])
                    else:
                        pass
            else:
                pass
                
        for i in ring:
            if len(ring[i]) == 3:
                count += 1
        
        return count
