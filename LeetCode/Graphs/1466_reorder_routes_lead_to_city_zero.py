"""
1466. Reorder Routes to Make All Paths Lead to the City Zero(Medium)

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Example 1:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
"""
from collections import defaultdict
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbors = defaultdict(list) # Used to convert the connection to Adjacency List(Graph Implementation)
        connection = set()
        print(neighbors)
        for source, destination in connections: # since its an undirected graph we simply add the node to both the
            # neighbors list
            neighbors[source].append(destination)
            neighbors[destination].append(source)
            connection.add((source, destination)) # Adding to set for faster lookup
        print(neighbors)
        # print(connection)
        curr = [0]              # Starrting the traversal from node 0 | follows bfs
        reverse = 0             # The counter keeping track of the routes reversed
        visited = set()         # a list to avoid already visited nodes
        visited.add(0)          # since we are starting with node 0 adding it to visited by default

        while curr:  # As long as there is a node to traverse, This condition is true
            print('curr : ', curr)
            new_curr = []#This would be helpful to stop the while loop in case we have visited all the nodes in the graph
            print('new_curr : ', new_curr)
            for city in curr: # iterates through the nodes in curr
                print('city : ', city)
                for n in neighbors[city]: # looks uo the neighboring nodes for the city
                    print('n : ', n)
                    if n not in visited:
                        print('adding to visited')
                        visited.add(n)
                        if (n, city) not in connection:
                            print('incrementing reverse')
                            reverse += 1
                        new_curr.append(n)
                print('[63] new_curr : ', new_curr)
                curr = new_curr
        return reverse

my_obj = Solution()
print(my_obj.minReorder(3, [[1,0],[2,0]]))
# print(my_obj.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))