class Vertex:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.graph = [None] * (self.v)

    def add_edge(self, src, dest):

        vertex = Vertex(dest)
        vertex.next = self.graph[src]
        self.graph[src] = vertex

        vertex = Vertex(src)
        vertex.next = self.graph[dest]
        self.graph[dest] = vertex

    def prints(self):
        print(1)
        for i in range(self.v):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 0)
    graph.add_edge(3, 1)
    graph.prints()

