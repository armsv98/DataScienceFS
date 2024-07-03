from typing import List

# Vectors
vector = List[float]

def add(v: vector, w: vector) -> vector:
    assert len(v) == len(w)
    return [v_i + w_i for v_i , w_i in zip(v,w)]

def subtract(v: vector, w: vector) -> vector:
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors: List[vector]) -> vector:
    assert vectors, "no vectors provided"
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes"
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

assert vector_sum([[2, 5], [4, 7], [3, 9]]) == [9, 21]


def scalar_multiply(c: float, v: vector) -> vector:
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[vector]) -> vector:
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [2, 3], [0, 4]]) == [1, 3]


def dot(v: vector, w: vector) -> float:
    assert len(v) == len(w)
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32

def sum_of_squares(v: vector) -> float:
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14


import math
def magnitude(v: vector) -> float:
    return math.sqrt(sum_of_squares(v))

assert magnitude([3, 4]) == 5


def squared_distance(v: vector, w: vector) -> float:
    return sum_of_squares(subtract(v, w))


def distance(v: vector, w: vector) -> float:
    return magnitude(subtract(v, w))


# Matrices
Matrix = List[List[float]]

A = [[1, 2, 4],
     [4, 5, 6]]

from typing import Tuple
def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0])
    return num_rows, num_cols

assert shape(A) == (2, 3)


def get_row(A: Matrix, i: int) -> vector:
    return A[i]

def get_col(A: Matrix, j: int) -> vector:
    return [row[j] for row in A]

from typing import Callable
def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i, j) for i in range(num_cols)] for j in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i,j: 1 if i == j else 0)

assert identity_matrix(2) == [[1,0],
                              [0,1]]
