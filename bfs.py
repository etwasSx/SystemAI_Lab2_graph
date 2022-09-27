from typing import List

from abstractClass import ABCClass
from collections import deque


class BFS(ABCClass):
    def find_shortest_path(self, start, end) -> List:
        start_idx, end_idx = self.set_default(start, end) # установка дефолтных методов
        k = deque()
        k.append(start_idx)
        while len(k) != 0:
            node = k.popleft()
            self.increment_iter_cnt()
            for city_idx, _ in self.adj_matrix[node]:  # Перебираем все вершины, соседние с node
                # Проверяем, если расстояние до city_idx больше, чем расстояние до node + 1
                if self.dist[city_idx] > self.dist[node] + 1:
                    self.dist[city_idx] = self.dist[node] + 1
                    k.append(city_idx) # будем работать с этой вершиной в будущем
                    self.parent[city_idx] = node # родитель текущей вершины - node

        path = self.build_path(end_idx)
        print('{}: {}'.format(self.get_method(), self.iteration_counter))
        return list(map(lambda x: self.idx_to_city[x], path))

    def get_method(self) -> str:
        return 'BFS'
