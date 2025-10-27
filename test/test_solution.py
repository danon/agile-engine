from ag.solution import solution

def test_example_1():
    assert solution('..B....B.BB') == 2

def test_example_2_space_in_left():
    assert solution('.BB.B.BBB...') == 2

def test_example_2_no_space_in_left():
    assert solution('BB.B.BBB...') == 4

def test_example_3():
    assert solution('.BBB.B') == -1

def test_case1_all_evens():
    assert solution('B.B.B.B.B.B.B.B.B.') == 0
    assert solution('B.B.B.B.B.B.B.B.B') == 0

def test_case1_all_odds():
    assert solution('.B.B.B.B.B.B.B.B.B.') == 0
    assert solution('.B.B.B.B.B.B.B.B.B') == 0

def test_example_4():
    assert solution('......B.B') == 0

def test_case1_valid():
    assert solution('B') == 0

def test_case2_valid_already_solved():
    assert solution('.B') == 0
    assert solution('B.') == 0
    assert solution('B.B') == 0
    assert solution('.B.B') == 0
    assert solution('B.B.') == 0
    assert solution('.B.B.') == 0
    assert solution('B.B.B') == 0
    assert solution('.B.B.B') == 0
    assert solution('B.B.B.') == 0
    assert solution('.B.B.B.') == 0

def test_invalid_1():
    assert solution('BB.') > -1
    assert solution('BB') == -1

def test_invalid_2():
    assert solution('BBB..') > -1
    assert solution('BBBB..') == -1

def test_invalid_3_valid():
    assert solution('BBB...') > -1
    assert solution('BBB..') > -1
    assert solution('BBB.') == -1

def test_invalid_4_invalid():
    assert solution('BBBB...') > -1

def test_invalid_5_valid():
    assert solution('B') > -1

def test_invalid_6_invalid():
    assert solution('BB') == -1
