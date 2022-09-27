from abstractClass import ABCClass


class DFS(ABCClass):
    def find_shortest_path(self, start, end):
        start_idx, end_idx = self.set_default(start, end)
        self.dfs(start_idx)
        path = self.build_path(end_idx)
        print('{}: {}'.format(self.get_method(), self.iteration_counter))
        return list(map(lambda x: self.idx_to_city[x], path))

    def dfs(self, node: int):
        self.increment_iter_cnt()
        for city_idx, _ in self.adj_matrix[node]:  # Перебираем всех соседей node
            if self.dist[city_idx] > 1 + self.dist[node]:  # Аналогично bfs
                self.dist[city_idx] = 1 + self.dist[node]
                self.parent[city_idx] = node
                self.dfs(city_idx)

    def get_method(self):
        return 'DFS'
