import argparse


def check_mod(i: int, nums: list) -> bool:
    """Check, if first param is dividable without
    reminder by any of the second params list of numbers.

    :param i: int to be checked
    :param nums: list of ints to check against
    :return: Returns True or False
    """
    for n in nums:
        if i % n == 0:
            return True
    return False


def sanitize_list_input(_list: list, _def: list) -> list:
    """Sanitize the _list by reducing it to distinct values.
    If _list is None, then return second parameters value _def

    :param _list: list, if not None, will be reduced to its distinct values
    :param _def: list, the value to be returned, if _list is None
    :return: Either sanitized _list or _def value, if _list is None
    """
    if not _list:
        return [_def]
    else:
        return list(set(_list))


def run(_start=1, _end=100, _fizz=None, _buzz=None) -> None:
    """Plays FuzzBuzz game.
    See https://en.wikipedia.org/wiki/Fizz_buzz for more info.

    :param _start: Whole number for start of sequence (Inclusive)
    :param _end: Whole number for end of sequence (Inclusive)
    :param _fizz: List of numbers Fizz is triggered
    :param _buzz: List of numbers Buzz is triggered
    :return: Does not return anything
    """
    _fizz = sanitize_list_input(_fizz, [3])
    _buzz = sanitize_list_input(_buzz, [5])

    for i in range(_start, _end + 1):
        output = ''
        output += 'Fizz' if check_mod(i, _fizz) else ''
        output += 'Buzz' if check_mod(i, _buzz) else ''

        print(str(i) if output == '' else output)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Simple FuzzBuzz algorithm with user definable rules',
    )
    parser.add_argument(
        '-s', '--start', type=int,
        help='Start of number sequence. Defaults to 1', default=1,
    )
    parser.add_argument(
        '-e', '--end', type=int,
        help='End of number sequence. Defaults to 99', default=99,
    )
    parser.add_argument(
        '-f', '--fizz', nargs='+', type=int,
        help='Fizz numbers. Defaults to 3', default=[3],
    )
    parser.add_argument(
        '-b', '--buzz', nargs='+', type=int,
        help='Buzz numbers. Defaults to 5', default=[5],
    )
    args = parser.parse_args()

    run(args.start, args.end, args.fizz, args.buzz)
