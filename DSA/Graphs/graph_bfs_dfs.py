from collections import deque


# Using Adjacency Matrix
class Graph_Using_Matrix:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertices = [''] * size

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertices[vertex] = data

    def print_graph(self):
        print('printing rows of the matrix')
        for row in self.adj_matrix:
            print(''.join(map(str, row)))
        for vertex,data in enumerate(self.vertices):
            print(f"{vertex} -> {data}")

    def bfs(self, start_node):
        queue = [self.vertices.index(start_node)]
        visited = [False] * self.size
        visited[queue[0]] = True
        while queue:
            current_vertex = queue.pop(0)
            print(self.vertices[current_vertex], end='')

            for i in range(self.size):
                if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
    def dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(self.vertices[vertex], end=' ')
        for i in range(self.size):
            if self.adj_matrix[vertex][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_node):
        visited = [False] * self.size
        start_vertex = self.vertices.index(start_node)
        self.dfs_util(start_vertex, visited)

obj1 = Graph_Using_Matrix(2)
# print(obj1.adj_matrix)
# print(obj1.size)
# print(obj1.vertices)
obj1.add_edge(0,0)
obj1.add_edge(1,1)
obj1.add_vertex(0,'A')
obj1.add_vertex(1,'B')


obj1.print_graph()
# obj1.add_edge(0,1)
# obj1.add_edge(0,1)



class Graph_Using_List:
    # def __init__(self):
    #     pass

    def graph_bfs(tree, start):
        visited = []
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                print(node, end=" ")

                for neighbor in tree[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)


    def graph_dfs(tree, start):
        pass

tree = {
    'A': ['B', 'C'],  # Node A connects to B and C
    'B': ['D', 'E'],  # Node B connects to D and E
    'C': ['F', 'G'],  # Node C connects to F and G
    'D': ['H', 'I'],  # Node D connects to H and I
    'E': ['J', 'K'],  # Node E connects to J and K
    'F': ['L', 'M'],  # Node F connects to L and M
    'G': ['N', 'O'],  # Node G connects to N and O
    'H': [], 'I': [], 'J': [], 'K': [],  # Leaf nodes have no children
    'L': [], 'M': [], 'N': [], 'O': []   # Leaf nodes have no children
}

obj2 = Graph_Using_List()
obj2.graph_bfs(tree,'A')



                                      [1,2,3]
                                    /         \
# choosing 1                  []                 [1]     left branch doesn't  choose 1| Right branch chooses 1
                           /    \               /    \
# choosing 2             []     [2]         [1]       [1,2]  left branch doesn't choose 2| Right branch chooses 2
                    /   \    /   \           /  \      /   \
# choosing 3     []    [3] [2] [2,3]      [1]  [1,3] [1,2]  [1,2,3] left branch doesn't choose 3| Right branch chooses 3