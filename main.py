"""
Author: Anthony Swierkosz
Date: 7/15/2022
"""


# I think this one works.
def find_in_range(start, end, x):
    """
    Finds if x is in the range of start and end.

    :param start: Start of range.
    :param end: End of range.
    :param x: Number to find.
    :return: True if x is in the range, False otherwise.
    """
    result = start <= x <= end

    if start > end:
        return not result
    else:
        return result

    # return not start <= x <= end if start > end else start <= x <= end


# I don't think this one works.
def is_in_range(start, end, x):
    return (x >= start and x <= end) or (x >= end and x <= start)


def main():
    print(find_in_range(30, 15, 14))
    # print(is_in_range(53, 7, 2))
    pass


if __name__ == '__main__':
    main()
