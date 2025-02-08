class Solution:
    
    def dfs(self, graph, cur_node, visited, path_visited, safe_nodes):
        visited[cur_node] = True
        path_visited[cur_node] = True
        
        for neighbor in graph[cur_node]:
            if not visited[neighbor]:
                if self.dfs(graph, neighbor, visited, path_visited, safe_nodes):
                    return True
            elif path_visited[neighbor]:  
                return True
        path_visited[cur_node] = False
        safe_nodes.add(cur_node)
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [False] * n
        path_visited = [False] * n
        safe_nodes = set()

        for i in range(n):
            if not visited[i]:
                self.dfs(graph, i, visited, path_visited, safe_nodes)
        return sorted(safe_nodes) 