from pytest import raises

from ag.solution import solution

# bucket size 1
def test_0_balls_in_1_size_bucket():
    with raises(Exception):
        solution('.')

def test_one_ball_in_1_size_bucket__does_not_need_moving():
    assert solution('B') == 0

# bucket size 2

def test_0_balls_in_2_size_bucket():
    with raises(Exception):
        solution('..')

def test_two_balls_in_2_size_bucket__is_not_solvable():
    assert solution('BB') == -1

# bucket size 3

def test_two_balls_in_three_size_bucket__is_solvable():
    assert solution('BB.') > -1

def test_two_balls_in_three_size_bucket__BBE_is_one_move():
    assert solution('BB.') == 1

def test_two_balls_in_three_size_bucket__EBB_is_one_move():
    assert solution('.BB') == 1

def test_two_balls_in_three_size_bucket__BEB_is_already_solved():
    assert solution('B.B') == 0

# bucket size 4

def test_three_balls_in_bucket_4__is_not_solvable():
    assert solution('BBB.') == -1

def test_two_balls_in_bucket_4__needs_1_move__both_at_front():
    assert solution('BB..') == 1

def test_two_balls_in_bucket_4__needs_1_move__both_at_back():
    assert solution('..BB') == 1

def test_two_balls_in_bucket_4__is_already_solved__from_start():
    assert solution('B.B.') == 0

def test_two_balls_in_bucket_4__needs_1_move__at_edges():
    assert solution('B..B') == 1

def test_two_balls_in_bucket_4__is_already_solved__from_end():
    assert solution('.B.B') == 0

def test_two_balls_in_bucket_4__needs_1_move__in_middle():
    assert solution('.BB.') == 1

# bucket size 5

def test_four_or_more_balls_in_bucket_5__is_not_solvable():
    assert solution('BBBBB') == -1
    assert solution('BBBB.') == -1

def test_three_balls_in_bucket_5__is_solvable():
    assert solution('BBB..') > -1

# bucket size 5 - chose 2

def test_two_balls_in_bucket_5__near__requires_one_move():
    assert solution('BB...') == 1

def test_two_balls_in_bucket_5__1_space__is_solved():
    assert solution('B.B..') == 0

def test_two_balls_in_bucket_5__1_space2__requires_1_move():
    assert solution('B..B.') == 1

def test_two_balls_in_bucket_5__1_space3__requires_1_move():
    assert solution('B...B') == 1

def test_two_balls_in_bucket_5__1_space__offset__is_solved():
    assert solution('.B.B.') == 0

# bucket size 5 - chose 3

def test_three_balls_in_bucket_5__spaces_out__are_solved():
    assert solution('B.B.B') == 0  # if balls are at max capacity, then they can only be spaced out to be solved

def test_three_balls_in_bucket_5__spaces_out__all_at_start__needs_one_move():
    assert solution('BBB..') == 1

def test_three_balls_in_bucket_5__spaces_out__all_at_back__needs_one_move():
    assert solution('..BBB') == 1

def test_three_balls_in_bucket_5__each_in_middle__needs_two_move():
    assert solution('.BBB.') == 2

def test_three_balls_in_bucket_5__one_off1__needs_one_move():
    assert solution('.BB.B') == 1

def test_three_balls_in_bucket_5__one_off2__needs_one_move():
    assert solution('B.BB.') == 1

def test_three_balls_in_bucket_5__two_spaces1__needs_one_move():
    assert solution('BB..B') == 1

def test_three_balls_in_bucket_5__two_spaces__needs_one_move():
    assert solution('B..BB') == 1
