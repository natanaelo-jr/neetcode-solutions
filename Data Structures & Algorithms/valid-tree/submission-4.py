class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # I can validate if the graph is a valid tree simply running a BFS
        # and counting the number of edges. If |E| == |V|-1 and all nodes are verified
        # then it's a valid tree

        # create the graph:
        graph = [set() for _ in range(n)]
        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]

            graph[v1].add(v2)
            graph[v2].add(v1)
        if n-1 != len(edges):
            return False
        
        visited = set()
        # run dfs or dfs whatever
        def dfs(current, father):
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor != father:
                    if neighbor in visited:
                        return False
                    else:
                        if not dfs(neighbor, current):
                            return False
            return True

        if not dfs(0, -1):
            return False
        return len(visited) == n 