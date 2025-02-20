""" Test cases for the parser """
import pytest
from ziffers import zparse, get_items

# pylint: disable=missing-function-docstring, line-too-long, invalid-name

def test_can_parse():
    expressions = [
        "0 1 2 3 4 5 6 7 8 9 T E",
        "023 i iv iv^min",
        "[1 [2 3]]",
        "(1 (1,3) 1..3)",
        "_^ q _qe^3 qww_4 _123 <1 2>",
        "q _2 _ 3 ^ 343",
        "2 qe2 e4",
        "q 2 <3 343>",
        "q (2 <3 343 (3 4)>)",
        "? 1 2",
        "(? 2 ? 4)+(1,4)",
        "(1 2 <2 3>)+(0 1 2)"
    ]
    results = []
    for expression in expressions:
        try:
            print(f"Parsing expression: {expression}")
            result = zparse(expression)
            results.append(True)
        except Exception as e:
            print(e)
            results.append(False)

    # Return true if all the results are true (succesfully parsed)
    print(results)
    assert all(results)


@pytest.mark.parametrize(
    "pattern",
    [
        "1 2 3",
        "q3 e4 s5",
    ],
)
def test_parsing_text(pattern: str):
    assert zparse(pattern).text == pattern

@pytest.mark.parametrize(
    "pattern,expected",
    [
        ("1 2 3", [1, 2, 3]),
        ("q2 eq3", [2, 3]),
    ],
)
def test_pitch_classes(pattern: str, expected: list):
    assert get_items(zparse(pattern),len(expected)*2,"pitch_class") == expected*2


@pytest.mark.parametrize(
    "pattern,expected",
    [
       ("__6 _0 _1 _2 _3 _4 _5 _6 0 1 2 3 4 5 6 ^0 ^1 ^2 ^3 ^4 ^5 ^6 ^^0", [-2, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2]),
       ("_ 1 _2 <3>3 ^^4", [-1, -2, 3, 1]),
       ("^ 1 ^1 3 _2 ^^1 _2 <-1> 2 ^4", [1, 2, 1, 0, 3, 0, -1, 0]),
    ]
)
def test_pitch_octaves(pattern: str, expected: list):
    assert get_items(zparse(pattern),len(expected)*2,"octave") == expected*2


@pytest.mark.parametrize(
    "pattern,expected",
    [
       ("w [1 [2 3]]", [0.5, 0.25, 0.25]),
       ("1.0 [1 [2 3]] 4 [3 [4 5]]", [0.5, 0.25, 0.25, 1.0, 0.5, 0.25, 0.25]),
       ("0.5 (0 0.25 3)+1", [0.5, 0.25]),
       ("[0 2 <2 8>:2 4] 0", [0.05, 0.05, 0.05, 0.05, 0.05, 0.25])
    ]
)
def test_subdivisions(pattern: str, expected: list):
    assert get_items(zparse(pattern),len(expected)*2,"duration") == expected*2

@pytest.mark.parametrize(
    "pattern,expected",
    [
       ("[: 1 [: 2 :] 3 :]", [62, 64, 64, 65, 62, 64, 64, 65]),
       ("(: 1 (: 2 :) 3 :)", [62, 64, 64, 65, 62, 64, 64, 65]),
       ("(1 2:2 3):2", [62, 64, 64, 65, 62, 64, 64, 65]),
       ("1:4",[62,62,62,62])
    ]
)
def test_repeats(pattern: str, expected: list):
    assert get_items(zparse(pattern),len(expected)*2,"note") == expected*2

@pytest.mark.parametrize(
    "pattern,expected",
    [
       ("[: 3 [2 4] :]", [0.25, 0.125, 0.125, 0.25, 0.125, 0.125]),
       ("[: 1 [2 [5 6]] 3 [2 4] :]", [0.25, 0.125, 0.0625, 0.0625, 0.25, 0.125, 0.125, 0.25, 0.125, 0.0625, 0.0625, 0.25, 0.125, 0.125]),
       ("(: 3 [2 4] :)", [0.25, 0.125, 0.125, 0.25, 0.125, 0.125]),
       ("(: 1 [2 [5 6]] 3 [2 4] :)", [0.25, 0.125, 0.0625, 0.0625, 0.25, 0.125, 0.125, 0.25, 0.125, 0.0625, 0.0625, 0.25, 0.125, 0.125]),
       ("(3 [2 4]):2", [0.25, 0.125, 0.125, 0.25, 0.125, 0.125]),
       ("(1 [2 [5 6]] 3 [2 4]):2", [0.25, 0.125, 0.0625, 0.0625, 0.25, 0.125, 0.125, 0.25, 0.125, 0.0625, 0.0625, 0.25, 0.125, 0.125]),

    ]
)
def test_repeat_durations(pattern: str, expected: list):
    assert get_items(zparse(pattern),len(expected)*2,"duration") == expected*2

@pytest.mark.parametrize(
    "pattern,expected",
    [
       ("0 [0 2] 0", [0.25, 0.125, 0.125, 0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125, 0.125, 0.25]),
       ("w 0 [0 [1 [2 3]] 0] 9", [1.0, 0.3333333333333333, 0.16666666666666666, 0.08333333333333333, 0.08333333333333333, 0.3333333333333333, 1.0, 1.0, 0.3333333333333333, 0.16666666666666666, 0.08333333333333333, 0.08333333333333333]),
       ("1.0 0 [[2 3] [3 5]] 4", [1.0, 0.25, 0.25, 0.25, 0.25, 1.0, 1.0, 0.25, 0.25, 0.25, 0.25, 1.0]),
       ("2.0 0 [1[2[3[4 5]6]7]8] 9", [2.0, 0.6666666666666666, 0.2222222222222222, 0.07407407407407407, 0.037037037037037035, 0.037037037037037035, 0.07407407407407407, 0.2222222222222222, 0.6666666666666666, 2.0, 2.0, 0.6666666666666666])

    ]
)
def test_looping_durations(pattern: str, expected: list):
    parsed = zparse(pattern)
    durations = []
    for i in range(12):
        durations.append(parsed[i].duration)
    assert durations == expected

@pytest.mark.parametrize(
    "pattern,expected",
    [
      ("e 1 | 3 | h 3 | e3 | 4", [0.125,0.25,0.5,0.125,0.25])
    ]
)
def test_measure_durations(pattern: str, expected: list):
    assert get_items(zparse(pattern),len(expected)*2,"duration") == expected*2

@pytest.mark.parametrize(
    "pattern,expected",
    [
      ("^ 1 | _ 3 | ^3 | 3 | _4", [1,-1,1,0,-1])
    ]
)
def test_measure_octaves(pattern: str, expected: list):
    assert get_items(zparse(pattern),len(expected)*2,"octave") == expected*2

@pytest.mark.parametrize(
    "pattern,expected",
    [
      ("e r qr r q r", [0.125, 0.25, 0.125, 0.25])
    ]
)
def test_rest(pattern: str, expected: list):
    assert get_items(zparse(pattern),len(expected)*2,"duration") == expected*2

@pytest.mark.parametrize(
    "pattern,expected",
    [
      ("-3..9 1..9", [55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 62, 64, 65, 67, 69, 71, 72, 74, 76])
    ]
)
def test_ranges(pattern: str, expected: list):
    assert get_items(zparse(pattern),len(expected)*2,"note") == expected*2

@pytest.mark.parametrize(
    "pattern,expected",
    [
      ("0 1 2 3", [None, 60, 62, 64])
    ]
)
def test_degree_notation(pattern: str, expected: list):
    assert get_items(zparse(pattern, degrees=True),len(expected)*2,"note") == expected*2

@pytest.mark.parametrize(
    "pattern,expected",
    [
      ("i ii iii iv v vi vii", [[60, 64, 67], [62, 65, 69], [64, 67, 71], [65, 69, 72], [67, 71, 74], [69, 72, 76], [71, 74, 77]])
    ]
)
def test_romans(pattern: str, expected: list):
    assert get_items(zparse(pattern),len(expected)*2,"note") == expected*2

@pytest.mark.parametrize(
    "pattern,expected",
    [
      ("[: i vi v :]", [[0, 2, 4], [5, 0, 2], [4, 6, 1], [0, 2, 4], [5, 0, 2], [4, 6, 1]]),
      ("i ii iii iv v vi vii", [[0, 2, 4], [1, 3, 5], [2, 4, 6], [3, 5, 0], [4, 6, 1], [5, 0, 2], [6, 1, 3]]),
      ("i^7 i^min iv^6", [[0, 2, 4, 6], [0, 2, 4], [3, 5, 0, 1]])
    ]
)
def test_romans_pcs(pattern: str, expected: list):
    assert get_items(zparse(pattern),len(expected)*2,"pitches") == expected*2

@pytest.mark.parametrize(
    "pattern,expected",
    [
     ("(i)+<0 1 2>", [[60, 64, 67], [62, 65, 69], [64, 67, 71], [60, 64, 67]]),
     ("(i)+<0 <1 2>>",[[60, 64, 67], [62, 65, 69], [60, 64, 67], [64, 67, 71]])
    ]
)
def test_cycles(pattern: str, expected: list):
    zparse.cache_clear() # Clear cache for cycles
    assert get_items(zparse(pattern),4,"note") == expected
