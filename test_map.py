from helpers import load_map
from student_code import shortest_path

MAP_40_ANSWERS = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5,  [5]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
]

def test_map_40():
    map_40 = load_map('map-40.pickle')
    correct = 0
    for start, goal, answer_path in MAP_40_ANSWERS:
        path = shortest_path(map_40, start, goal)

        print("For start:", start, 
                  "Goal:     ", goal,
                  "Your path:", path,
                  "Correct:  ", answer_path)

        assert path == answer_path
    