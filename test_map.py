from student_code import load_map, shortest_path, dist, reconstruct_path
from math import isclose

MAP_40_ANSWERS = [
    (5, 34, [5, 16, 37, 12, 34]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24]),
]
map_40 = load_map('map-40.pickle')

def test_distance():
    # Test Euclidean distance calculation
    x = [0.0, 0.0]
    y = [3.0, 4.0]

    assert isclose(dist(x,x), 0.0)
    assert isclose(dist(x,y), 5.0)

def test_reconstruct():
    # Test function to reconstruct path
    came_from = {1: 2, 2: 3, 3: 5, 4: 3}

    assert reconstruct_path(came_from, 1) == [5, 3, 2, 1]
    assert reconstruct_path(came_from, 4) == [5, 3, 4]
    assert reconstruct_path(came_from, 5) == [5]

def test_simple_path():
    # Test single point
    path = shortest_path(map_40, 5, 5)
    assert path == [5]

def test_map_40():
    # Run through each path in larger map
    for start, goal, answer_path in MAP_40_ANSWERS:
        assert shortest_path(map_40, start, goal) == answer_path
    