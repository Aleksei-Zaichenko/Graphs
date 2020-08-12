from util import Queue
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])

    q = Queue()
    q.enqueue([starting_node])
    max_path_length = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

            if len(path_copy) >= max_path_length:
                earliest_ancestor = path_copy[-1]
                max_path_length = len(path_copy)

    return earliest_ancestor


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors,1))
print(earliest_ancestor(test_ancestors, 10))
print(earliest_ancestor(test_ancestors,6))
