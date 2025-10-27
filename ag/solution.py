def solution(input: str) -> int:
    balls_count = input.count('B')
    spaces_count = input.count('.')

    if balls_count == 0:
        raise Exception('no balls in the bucket')
    if balls_count == 1:
        return 0
    if balls_count > spaces_count + 1:
        return -1
    evens, odds = __parity_analysis(input)
    if evens == 0:
        return 0

    if evens == 1 and odds == 1:
        return 1

    return 0

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
