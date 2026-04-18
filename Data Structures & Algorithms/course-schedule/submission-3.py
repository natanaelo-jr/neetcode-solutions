class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [set() for _ in range(numCourses)]
        for prerequisite in prerequisites:
            course = prerequisite[0]
            dependency = prerequisite[1]
            graph[course].add(dependency)

        visited = set()
        checked = set()
        
        def dfs(course_index):
            if course_index in checked:
                return False

            if course_index in visited:
                return True
            
            checked.add(course_index)
            for dependency in graph[course_index]:
                if not dfs(dependency):
                    return False
            checked.remove(course_index)
            visited.add(course_index)
            return True

        for i in range(len(graph)):
            if not dfs(i):
                return False

        return True