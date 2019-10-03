"""T06."""


def common_end(a, b):
    """
    Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.

    Both arrays will be length 1 or more.

    common_end([1, 2, 3], [7, 3]) → True
    common_end([1, 2, 3], [7, 3, 2]) → False
    common_end([1, 2, 3], [1, 3]) → True
    :param a: List of integers.
    :param b: List of integers.
    :return: The last or the first elements are the same.
    """
    if len(a) >= 1 and len(b) >= 1:
        for item in a and b:
            if item[0] in a == item[0] in b:
                return True


def alarm_clock(day, vacation):
    """
    Return what time the alarm clock should be set.

    Given a day of the week encoded as 0=Mon, 1=Tue, ... 5=Sat, 6=Sun
    and a boolean indicating if we are on vacation,
    return a string of the form "08:00" indicating when the alarm clock should ring.

    Weekdays, the alarm should be "08:00" and on the weekend it should be "10:00".
    Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

    alarm_clock(1, False) → '08:00'
    alarm_clock(3, False) → '08:00'
    alarm_clock(6, False) → '10:00'

    :param day: Day of week.
    :param vacation: Whether it is vacation.
    :return: String when to set alarm clock.
    """
    pass


def without_end(s):
    """
    Given a string, return a version without the first and last char, so "Hello" yields "ell".

    The string length will be at least 2.

    without_end('Hello') → 'ell'
    without_end('java') → 'av'
    without_end('coding') → 'odin'

    :param s: String
    :return: String without first and last char.
    """
    pass


def index_index_value(nums):
    """
    Return value at index.

    Take the last element.
    Use the last element value as the index to get another value.
    Use this another value as the index of yet another value.
    Return this yet another value.

    If the the last element points to out of list, return -1.
    If the element at the index of last element points out of the list, return -2.

    All elements in the list are non-negative.

    index_index_value([0]) => 0
    index_index_value([0, 2, 4, 1]) => 4
    index_index_value([0, 2, 6, 2]) => -2  (6 is too high)
    index_index_value([0, 2, 4, 5]) => -1  (5 is too high)

    :param nums: List of integer
    :return: Value at index of value at index of last element's value
    """
    pass


def mirror_ends(s):
    """
    Given a string, look for a mirror image (backwards) string at both the beginning and end of the given string.

    In other words, zero or more characters at the very beginning of the given string,
    and at the very end of the string in reverse order (possibly overlapping).

    For example, the string "abXYZba" has the mirror end "ab".

    mirrorEnds("abXYZba") → "ab"
    mirrorEnds("abca") → "a"
    mirrorEnds("aba") → "aba"

    :param s: String
    :return: Mirror image string
    """
    pass


if __name__ == '__main__':
    print(common_end([1, 2, 3], [7, 3]))
    print(alarm_clock(1, False))
    print(without_end('Hello'))
    print(index_index_value([0, 2, 4, 1]))
    print(mirror_ends("abXYZba"))
