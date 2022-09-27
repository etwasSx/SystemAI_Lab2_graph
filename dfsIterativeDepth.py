from abstractClass import ABCClass


class DFSIterativeDepth(ABCClass):
    # Весь алгорит аналогичен обычному dfs, просто теперь добавляется максимальная глубина, достигнув которую, мы возвращаемся назад по рекурсии
    max_depth: int = 0

    def find_shortest_path(self, start, end):
        self.used = [0 for _ in range(self.n)]
        start_idx, end_idx = self.set_default(start, end)
        self.depth_assessment(start_idx)
        for depth in range(1, self.max_depth + 1):
            self.dfs_with_depth(start_idx, depth)
            print('{} = {}: {}'.format(self.get_method(), depth, self.iteration_counter))
            self.set_default(start, end)
        path = self.build_path(end_idx)
        return list(map(lambda x: self.idx_to_city[x], path))

    def depth_assessment(self, node, depth=1):  # Этот метод находит максимальную глубину дерева(глубина - self.max_depth)
        self.used[node] = 1
        self.max_depth = max(self.max_depth, depth)
        for city_idx, distance in self.adj_matrix[node]:
            if self.used[city_idx] == 0:
                self.depth_assessment(city_idx, depth + 1)

    def dfs_with_depth(self, node, depth):
        if depth <= 0:
            return
        self.increment_iter_cnt()
        for city_idx, _ in self.adj_matrix[node]:
            if self.dist[city_idx] > self.dist[node] + 1:
                self.dist[city_idx] = self.dist[node] + 1
                self.parent[city_idx] = node
                self.dfs_with_depth(city_idx, depth - 1)

    def get_method(self):
        return 'DFS с итеративным углублением'
