from collections import deque

from abstractClass import ABCClass


class BidirectionalSearch(ABCClass):  # Алгоритм аналогичен обычному bfs, только здесь мы идём не от одной вершины ко всем, а от одной, до другой, и как только их пути пересекаются, мы прекращаем поиск пути
    def find_shortest_path(self, start, end):
        self.used = [0 for _ in range(self.n)]
        start_idx, end_idx = self.set_default(start, end)
        k = deque()
        k.append((start_idx, False))  # В сравнении с обычным bfs, мы добавили новый флаг - is_reversed, который показывает, с какого направления мы делаем текущий шаг(если шаг идёт от начала, то флаг имеет одно значение, если от конца, то другое)
        k.append((end_idx, True))
        flag = False
        while len(k) != 0 and not flag:
            node, is_reversed = k.popleft()
            self.increment_iter_cnt()
            for city_idx, _ in self.adj_matrix[node]:
                if not self.used[city_idx]:  # Если в текущую вершину мы ещё не заходили, то мы заходим в неё и указываем, с какой стороны мы пришли к ней
                    self.used[city_idx] = 1 if is_reversed else 2
                    self.dist[city_idx] = self.dist[node] + 1
                    k.append((city_idx, is_reversed))
                if self.used[city_idx] == (2 if is_reversed else 1):  # Если наши пути пересеклись с другим путём, то значит мы нашли самый короткий путь от одной вершины к другой
                    flag = True
                    break
        print('{}: {}'.format(self.get_method(), self.iteration_counter))
        return ''

    def get_method(self):
        return 'Двунаправленный поиск'

