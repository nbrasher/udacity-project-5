from math import isclose
from helpers import load_map
from student_code import shortest_path, get_distance

MAP_40_ANSWERS = [
    (5, 34, [5, 16, 37, 12, 34]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24]),
]
map_40 = load_map('map-40.pickle')

def test_distance():
    # Test Euclidean distance calculation
    x = [0.0, 0.0]
    y = [3.0, 4.0]

    assert isclose(get_distance(x,x), 0.0)
    assert isclose(get_distance(x,y), 5.0)

def test_simple_path():
    # Test single point
    path = shortest_path(map_40, 5, 5)
    assert path == [5]

def test_map_40():
    # Run through each path in larger map
    for start, goal, answer_path in MAP_40_ANSWERS:
        assert shortest_path(map_40, start, goal) == answer_path
    