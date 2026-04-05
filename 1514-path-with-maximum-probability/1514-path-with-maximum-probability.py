import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        # Build adjacency list
        adjM = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            adjM[u].append((v, p))
            adjM[v].append((u, p))
        
        # Python's heapq is a Min-Heap. 
        # We multiply probabilities by -1 to simulate a Max-Heap.
        pq = [(-1.0, start_node)]
        
        maxP = defaultdict(float)
        maxP[start_node] = 1.0
        
        while pq:
            prob, curr = heapq.heappop(pq)
            prob = -prob # Convert back to positive
            
            # If we reached the target, we are done
            if curr == end_node:
                return prob
                
            # Optimization: Skip if we've already found a better path to this node
            if prob < maxP[curr]:
                continue
                
            for adj, edge_prob in adjM[curr]:
                new_prob = prob * edge_prob
                
                if new_prob > maxP[adj]:
                    maxP[adj] = new_prob
                    heapq.heappush(pq, (-new_prob, adj))
                    
        return 0.0