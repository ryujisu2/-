import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1

def kruskal(graph):
    min_heap = []
    for u, v, w in graph:
        heapq.heappush(min_heap, (w, u, v))

    n = len(set(v for u, v, w in graph))
    union_find = UnionFind(n)
    result = []

    while len(result) < n - 1:
        weight, u, v = heapq.heappop(min_heap)
        if union_find.find(u) != union_find.find(v):
            result.append((u, v, weight))
            union_find.union(u, v)

    return result

# Example usage:
graph = [(0, 1, 7), (0, 3, 5), (1, 2, 8), (1, 3, 9), (1, 4, 7), (2, 4, 5), (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)]
minimum_spanning_tree = kruskal(graph)
print(minimum_spanning_tree)
