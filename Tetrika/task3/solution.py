from datetime import datetime


def appearance(intervals: dict[str, list[int]]) -> int:
    result = []
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    pupil_interval = [(pupil[i], pupil[i + 1]) for i in range(0, len(pupil), 2)]
    tutor_interval = [(tutor[i], tutor[i + 1]) for i in range(0, len(tutor), 2)]
    lesson_start, lesson_end = lesson[0], lesson[-1]

    def get_intersection(intervals: [(int, int)]) -> list[(int, int)]:
        intersection = []
        for start, end in intervals:
            if end > lesson_start and start < lesson_end:
                intersection_start = max(start, lesson_start)
                intersection_end = min(end, lesson_end)
                intersection.append((intersection_start, intersection_end))
        return intersection
    pupil_intersections = get_intersection(pupil_interval)
    tutor_intersections = get_intersection(tutor_interval)

    intersection_time = 0
    for p_start, p_end in pupil_intersections:
        for t_start, t_end in tutor_intersections:
            start = max(p_start, t_start)
            end = min(p_end, t_end)
            if end > start:
                intersection_time += (end - start)
    print(intersection_time)
    return intersection_time

tests = [

    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },

]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
