class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()
        count = 0
        for i in range(n):
            if i in visited:
                continue
            
            count +=1
            queue = deque([i])
            visited.add(i)

            while queue:
                curr = queue.popleft()
                for nei in adj[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
        return count

        