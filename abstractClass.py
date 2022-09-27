from abc import ABC, abstractmethod
from typing import List, Dict


class ABCClass(ABC):
    adj_matrix: List[tuple]
    city_to_idx: Dict
    idx_to_city: Dict
    n: int
    dist: List
    parent: List
    iteration_counter: int = 0

    def __init__(self, adj_matrix: List, city_to_idx: Dict, idx_to_city: Dict):
        self.adj_matrix = adj_matrix.copy()
        self.city_to_idx = city_to_idx.copy()
        self.idx_to_city = idx_to_city
        self.n = len(city_to_idx)

    def set_default(self, start, end):  # Метод устанавливающий дефолтные значения
        self.dist = [float('+inf') for _ in range(self.n)]  # Дистанция от начального положения, до всех вершин
        self.parent = [-1 for _ in range(self.n)]  # Родители для вершин
        start_idx = self.city_to_idx[start]  # Индекс начального города(из условия задачи)
        end_idx = self.city_to_idx[end]  # Индекс конечного города(из условия задачи)
        self.dist[start_idx] = 0
        self.iteration_counter = 0  # Количество итераций, которое выполнил метод(нужно для таблички)
        return start_idx, end_idx

    def increment_iter_cnt(self):  # Метод для более понятной визуализации процесса увеличения счётчика итераций
        self.iteration_counter += 1

    def build_path(self, start_idx) -> List:  # Метод строющий путь, используя список родителей вершин
        path = []
        cur_city = start_idx
        while self.parent[cur_city] != -1:
            path.append(cur_city)
            cur_city = self.parent[cur_city]
        path.append(cur_city)
        return reversed(path)

    @abstractmethod
    def find_shortest_path(self, start, end):  # Абстрактный метод для нахождения кратчайшего пути
        pass

    @abstractmethod
    def get_method(self):  # Метод, возвращающий название метода
        pass

