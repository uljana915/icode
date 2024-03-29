# -*- coding: utf-8 -*-
"""Check if given ID code is valid."""
id_code = ''


def is_valid_gender_number(gender_number: int) -> bool:
    # gender_number = int(id_code[0])
    if gender_number in range(1, 7):
        return True
    else:
        return False


def is_leap_year(year_number: int) -> bool:
    if year_number % 4 != 0 or (year_number % 100 == 0 and year_number % 400 != 0):
        return False
    else:
        return True


def get_gender(gender_number: int) -> str:
    # gender_number = int(id_code[0])
    if gender_number in {1, 3, 5}:
        return "Male"
    elif gender_number in {2, 4, 6}:
        return "Female"


def is_valid_year_number(year_number: int) -> bool:
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    # year_number = int(id_code[1:3])
    if 0 <= year_number <= 99:
        return True
    else:
        return False


def is_valid_month_number(month_number: int) -> bool:
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    # month_number[3:5]
    if 1 <= month_number <= 12:
        return True
    else:
        return False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """
    Check if given value is correct for day number in ID code.
    Also, consider leap year and which month has 30 or 31 days.

    :param gender_number: int
    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    pass


def is_valid_birth_number(birth_number: int):
    """
    Check if given value is correct for birth number in ID code.

    :param birth_number: int
    :return: boolean
    """
    pass


def is_valid_control_number(id_code: str) -> bool:
    """
    Check if given value is correct for control number in ID code.
    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    pass


def get_full_year(gender_number: int, year_number: int) -> int:
    """
    Define the 4-digit year when given person was born.
    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year_number: int
    :return: int
    """
    if gender_number == 1 or 2:
        return int("18" + str(year_number))
    elif gender_number == 3 or 4:
        return int("19" + str(year_number))
    elif gender_number == 5 or 6:
        return int("20" + str(year_number))
    else:
        return False


def get_birth_place(birth_number: int) -> str:
    """
    Find the place where the person was born.

    Possible locations are following: Kuressaare, Tartu, Tallinn, Kohtla-Järve, Narva, Pärnu,
    Paide, Rakvere, Valga, Viljandi, Võru and undefined. Lastly if the number is incorrect the function must return
    the following 'Wrong input!'
    :param birth_number: int
    :return: str
    """
# 001...010 = Kuressaare
# 011...020 = Tartu
# 021...220 = Tallinn
# 221...270 = Kohtla-Järve
# 271...370 = Tartu
# 371...420 = Narva
# 421...470 = Pärnu
# 471...490 = Tallinn
# 491...520 = Paide
# 521...570 = Rakvere
# 571...600 = Valga
# 601...650 = Viljandi
# 651...710 = Võru
# 711...999 = undefined
    # 6/00/06/28/221/7
# birth_number[7:10]
    birth_place = {
        range(1, 11) : "Kuressaare",
        range(11, 21) : "Tartu",
        range(21, 221) : "Tallinn",
        range(221, 271) : "Kohtla-Järve",
        range(271, 371) : "Tartu",
        range(371, 421) : "Narva",
        range(421, 471) : "Pärnu",
        range(471, 491) : "Tallinn",
        range(491, 521) : "Paide",
        range(521, 571) : "Rakvere",
        range(571, 601) : "Valga",
        range(601, 651) : "Viljandi",
        range(651, 711) : "Võru",
        range(711, 999) : "undefined"
    }



def get_data_from_id(id_code: str) -> str:
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    :param id_code: str
    :return: str
    """
    pass


def is_id_valid(id_code: str) -> bool:
    """
    Check if given ID code is valid and return the result (True or False).

    Complete other functions before starting to code this one.
    You should use the functions you wrote before in this function.
    :param id_code: str
    :return: boolean
    """
    pass


if __name__ == '__main__':
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False
    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> true
    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False
    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False
    print("\nFebruary check:")
    print(
        is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)
    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True
    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6

    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    # Comment these back in if you have completed other functions.
    print("\nChecking where the person was born")

    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"

    print("\nOverall ID check::")
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("12345678901"))  # -> False
    print("\nTest now your own ID code:")
    personal_id = input()  # type your own id in command prompt
    print(is_id_valid(personal_id))  # -> True

