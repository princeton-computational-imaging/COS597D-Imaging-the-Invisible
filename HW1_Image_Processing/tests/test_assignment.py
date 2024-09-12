import random
import numpy as np

def test_indexing_aggregation():
    from src import indexing_aggregation

    n = np.random.randint(low=1, high=10)
    x = np.random.random(10)

    assert np.isclose(indexing_aggregation(x, n), x[:n].mean())

def test_create_add_matrix():
    from src import create_add_matrix
    x = np.random.random((3, 3))
    y = create_add_matrix(x) - x
    ones = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    assert np.allclose(y, ones)

def test_sum_numbers():
    from src import sum_numbers
    for i in range(100):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        assert sum_numbers(x, y) == (x + y)

def test_multiply_numbers():
    from src import multiply_numbers
    for i in range(100):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        assert multiply_numbers(x, y) == (x * y)
