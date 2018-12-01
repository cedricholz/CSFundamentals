import heapq


# O(E + Vlog(V))
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u in self.graph:
            self.graph[u].append((v, w))
        else:
            self.graph[u] = [(v, w)]

    def dijkstras(self, s):
        distances = {}

        # Set all distances to infinity
        for key in self.graph:
            distances[key] = float("inf")
        for graph_list in self.graph.values():
            for val in graph_list:
                distances[val[0]] = float("inf")
        distances[s] = 0

        h = []

        heapq.heappush(h, (0, s))
        while h:
            cur_distance, cur_node = heapq.heappop(h)

            if cur_node in self.graph:
                for edge in self.graph[cur_node]:
                    end_node, to_node_distance = edge

                    total_distance_to_node = cur_distance + to_node_distance

                    if total_distance_to_node < distances[end_node]:
                        distances[end_node] = total_distance_to_node

                        heapq.heappush(h, (total_distance_to_node, end_node))
        print(distances)


g = Graph()
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 2)

g.add_edge("B", "C", 3)
g.add_edge("B", "D", 2)
g.add_edge("B", "E", 3)

g.add_edge("C", "B", 1)
g.add_edge("C", "D", 4)
g.add_edge("C", "E", 5)

g.add_edge("E", "D", 1)

g.dijkstras("A")
