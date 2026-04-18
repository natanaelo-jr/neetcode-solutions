class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        def getIndex(i, j):
            return i*N + j

        def getNeighbours(i, j):
            neighbours = list()
            if i > 0 and grid[i-1][j] == '1':
                neighbours.append((i-1, j))
            if j > 0 and grid[i][j-1] == '1':
                neighbours.append((i,j-1))
            if i < M-1 and grid[i+1][j] == '1':
                neighbours.append((i+1,j))
            if j < N-1 and grid[i][j+1] == '1':
                neighbours.append((i, j+1))
            return neighbours
        

        visited = set()
        islands = 0

        def explore(i, j):
            visited.add(getIndex(i,j))
            for neighbour in getNeighbours(i,j):
                neighbour_index = getIndex(neighbour[0], neighbour[1])
                if neighbour_index not in visited:
                    explore(neighbour[0], neighbour[1])

        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1' and getIndex(i,j) not in visited:
                    islands += 1
                    explore(i,j)
                    print(visited)

        return islands