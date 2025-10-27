def solution(input: str) -> int:
    if not __valid_input(input):
        return -1
    number_of_balls_balls = input.count('B')
    how_many_you_have_to_move = number_of_balls_balls - how_many_can_stay(input)
    return how_many_you_have_to_move

def how_many_can_stay(input: str) -> int:
    evens = 0
    odds = 0
    for index, char in enumerate(input):
        if char == 'B':
            if index % 2 == 0:
                evens += 1
            else:
                odds += 1

    if evens == 0:
        return odds  # all odds can stay
    if odds == 0:
        return evens  # all evens can stay

    if evens > odds:
        return evens  # all evens can stay
    if odds > evens:
        return odds  # all odds can stay
    if odds == evens:
        return odds
    return -2000

def __valid_input(input: str) -> int:
    balls = input.count('B')
    empty = input.count('.')
    return balls - 1 <= empty
