from abc import ABC, abstractmethod
from typing import List, Dict


class ABCClass(ABC):
    adj_matrix: List[tuple] #список смежности
    city_to_idx: Dict #словарь. Слева город, справа индекс
    idx_to_city: Dict #Тоже что и выше, но наоборот
    n: int
    dist: List  #вес ребер
    parent: List #список родителей
    iteration_counter: int = 0 #Сколько сделано шагов(итераций) для нахождения искомого города

    # Конструктор
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
        self.dist[start_idx] = 0 # Начальный город
        self.iteration_counter = 0  # Количество итераций, которое выполнил метод(нужно для таблички)
        return start_idx, end_idx

    def increment_iter_cnt(self):  # Метод для более понятной визуализации процесса увеличения счётчика итераций
        self.iteration_counter += 1

    def build_path(self, start_idx) -> List:  # Метод строющий путь, используя список родителей вершин
        path = []
        cur_city = start_idx # стартовый город, его индекс
        while self.parent[cur_city] != -1: # Пока есть родитель
            path.append(cur_city) # Добавляем в путь индекс текущего города
            cur_city = self.parent[cur_city] # переходим к родителю
        path.append(cur_city)
        return reversed(path)

    @abstractmethod
    def find_shortest_path(self, start, end):  # Абстрактный метод для нахождения кратчайшего пути
        pass

    @abstractmethod
    def get_method(self):  # Метод, возвращающий название метода
        pass

