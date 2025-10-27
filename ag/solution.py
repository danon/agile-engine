def solution(input: str) -> int:
    balls_count = input.count('B')
    spaces_count = input.count('.')
    if balls_count == 0:
        raise Exception('no balls in the bucket')
    if balls_count > spaces_count + 1:
        return -1
    if balls_count == 1:
        return _strategy_1_ball()
    if balls_count == 2:
        return _strategy_2_balls(input)
    if balls_count == 3:
        return _strategy_3_balls(input)
    raise Exception('Not implemented')

def _strategy_1_ball():
    return 0

def _strategy_2_balls(input: str) -> int:
    space_between_them = space_between_2_balls(input)
    if space_between_them == 2:
        return 0
    return 1

def _strategy_3_balls(input: str) -> int:
    evens, odds = __parity_analysis(input)
    return min(evens, odds)

def space_between_2_balls(input: str) -> int:
    first = input.index('B')
    second = input.rindex('B')
    return second - first

def __parity_analysis(input: str) -> tuple[int, int]:
    evens = 0
    odds = 0
    for index, char in enumerate(input):
        if char == 'B':
            if index % 2 == 0:
                evens += 1
            else:
                odds += 1
    return evens, odds
