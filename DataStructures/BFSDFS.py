import queue


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def BFS(self, s):

        visited = set()
        visited.add(s)

        q = queue.Queue()
        q.put(s)

        while not q.empty():
            cur_node = q.get()
            print(cur_node)
            for i in self.graph[cur_node]:
                if i not in visited:
                    q.put(i)
                    visited.add(i)

    def DFS(self, s):
        visited = set()

        def h(v, visited):
            print(v)
            visited.add(v)
            for i in self.graph[v]:
                if i not in visited:
                    h(i, visited)

        h(s, visited)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.BFS(2)
g.DFS(2)
