from typing import List

from abstractClass import ABCClass


class DFSWithDepth(ABCClass):
    # Всё аналогично dfs с итеративной глубиной, только здесь мы глубину не перебираем
    used: List
    max_depth: int = 0

    def find_shortest_path(self, start, end):
        self.used = [0 for _ in range(self.n)]
        start_idx, end_idx = self.set_default(start, end)
        self.depth_assessment(start_idx)
        self.dfs_with_depth(start_idx, self.max_depth)
        path = self.build_path(end_idx)
        print('{}: {}'.format(self.get_method(), self.iteration_counter))
        return list(map(lambda x: self.idx_to_city[x], path))

    def depth_assessment(self, node, depth=1):
        self.used[node] = 1
        self.max_depth = max(self.max_depth, depth)
        for city_idx, distance in self.adj_matrix[node]:
            if self.used[city_idx] == 0:
                self.depth_assessment(city_idx, depth + 1)

    def dfs_with_depth(self, node, depth):
        self.increment_iter_cnt()
        if depth <= 0:
            return
        for city_idx, _ in self.adj_matrix[node]:
            if self.dist[city_idx] > self.dist[node] + 1:
                self.dist[city_idx] = self.dist[node] + 1
                self.parent[city_idx] = node
                self.dfs_with_depth(city_idx, depth - 1)

    def get_method(self):
        return 'DFS с ограничением глубины'
