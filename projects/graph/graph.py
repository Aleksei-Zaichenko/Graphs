"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        queue = Queue()

        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            u = queue.dequeue()

            if u not in visited:
                print(u)
                visited.add(u)
                for neighbor in self.vertices[u]:
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = []
        stack = Stack()

        stack.push(starting_vertex)

        while stack.size() > 0:
            s = stack.pop()

            if s not in visited:
                visited.append(s)
                print(s)
                for neighbor in self.vertices[s]:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()

        def DFT(vertex):
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_neighbor in self.vertices[vertex]:
                    DFT(next_neighbor)

        DFT(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = set()

        queue.enqueue([starting_vertex])

        while queue.size() > 0:
            path = queue.dequeue()
            lastVertex = path[len(path) - 1]

            if lastVertex not in visited:
                if lastVertex == destination_vertex:
                    return path
                visited.add(lastVertex)

                for neighbor in self.vertices[lastVertex]:

                    pathCopy = path.copy()
                    pathCopy.append(neighbor)
                    queue.enqueue(pathCopy)

        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()

        stack.push([starting_vertex])

        while stack.size() > 0:
            path = stack.pop()
            lastVertex = path[len(path) - 1]

            if lastVertex not in visited:
                if lastVertex == destination_vertex:
                    return path
                visited.add(lastVertex)
                for neighbor in self.vertices[lastVertex]:
                    pathCopy = path.copy()
                    pathCopy.append(neighbor)
                    stack.push(pathCopy)

        return None

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        visited = set()

        def DFT(vertex, path=[]):
            if vertex not in visited:
                visited.add(vertex)
                path.append(vertex)
                if path[len(path) - 1] == destination_vertex:
                    return path

                for next_neighbor in self.get_neighbors(vertex):
                    if next_neighbor not in visited:
                        pathCopy = path.copy()
                        newPath = DFT(next_neighbor, pathCopy)
                        if newPath:
                            return newPath

        return DFT(starting_vertex)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print('\n')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
