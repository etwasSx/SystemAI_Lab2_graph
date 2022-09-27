from typing import List

from abstractClass import ABCClass


class FirstBestMatch(ABCClass):  # Алгоритм максимально тупой, мы просто на каждом шаге выбираем ребро с минимальным весом, если мы зашли в тупик, то просто возвращаемся назад по рекурсии и выбираем второе по велечине ребро
    used: List
    path: List = []
    flag: bool = False  # Он нужен для того, чтобы остановить рекурсию, когда мы дошли до нашей конечной точки(end_idx)
    end_idx: int

    def find_shortest_path(self, start, end):
        self.used = [0 for _ in range(self.n)]
        start_idx, end_idx = self.set_default(start, end)
        self.end_idx = end_idx
        self.path.append((start, 0))
        self.first_best_match_dfs(start_idx)
        print('{}: {}'.format(self.get_method(), self.iteration_counter))
        return self.path

    def first_best_match_dfs(self, node):  # В целом, алгоритм очень похож на классический dfs, только теперь мы переходим в вершины по увеличению расстояния до них(т.е. сначала перейдём в вершину, до которой самое короткое ребро из текущей вершины и т.д.)
        if self.flag:
            return
        if node == self.end_idx:
            self.flag = True
            return
        node_arr = []
        self.used[node] = 1
        self.increment_iter_cnt()
        for city_idx, distance in self.adj_matrix[node]:
            if not self.used[city_idx]:
                node_arr.append((city_idx, distance))
        node_arr.sort(key=lambda a: a[1])
        for city_idx, distance in node_arr:
            self.path.append((self.idx_to_city[city_idx], distance))
            self.first_best_match_dfs(city_idx)
            if self.flag:
                break
            self.path.pop()

    def get_method(self):
        return 'Первое наилучшее соответствие'
