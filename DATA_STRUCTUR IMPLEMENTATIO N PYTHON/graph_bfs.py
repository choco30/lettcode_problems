from collections import deque
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)
    def print(self):
        print(self.graph)

    def bfs(self):
        visited = [False] * (max(self.graph)+1)
        for i in self.graph:
           if not visited[i]:
                queue = deque()

                # Mark the source node as
                # visited and enqueue it
                queue.append(i)
                visited[i] = True

                while queue:

                    # Dequeue a vertex from
                    # queue and print it
                    s = queue.popleft()
                    print(s, end=" ")

                    # Get all adjacent vertices of the
                    # dequeued vertex s. If a adjacent
                    # has not been visited, then mark it
                    # visited and enqueue it
                    for j in self.graph[s]:
                        if visited[j] == False:
                            queue.append(j)
                            visited[j] = True


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.add_edge(2,9)
print("Following is Breadth First Traversal")
g.print()
g.bfs()
