class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [set() for _ in range(numCourses)]
        for prerequisite in prerequisites:
            course = prerequisite[0]
            dependency = prerequisite[1]
            graph[course].add(dependency)

        visited = set()
        checked = set()
        isValid = [True]
        
        def dfs(course_index, checked, valid):
            if valid[0] == False:
                return
            if course_index in checked:
                valid[0] = False
                return 

            if course_index in visited:
                return
            
            checked.add(course_index)
            for dependency in graph[course_index]:
                dfs(dependency, checked, valid)
            checked.remove(course_index)
            visited.add(course_index)
            return

        for i in range(len(graph)-1):
            dfs(i, checked, isValid)

        return isValid[0]