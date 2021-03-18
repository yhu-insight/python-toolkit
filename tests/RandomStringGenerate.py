# -*- coding: utf-8 -*-

# Python Random String Password
# Author - yucheng.hu@insight.com

import string
from random import choice


def random_password(length, printable):
    """
    Provides a Random String of the given length.
    :param printable: The string for Random String
    :param int length: The length of the password to generate.
    """

    return "".join([choice(printable) for x in range(int(length))])


if __name__ == "__main__":
    3

amount = int(input("How many Random String: "))
number = int(input("Length of Random String? "))

for i in range(1, amount + 1):
    print(f"   Random String [Printable String]: {i} - {repr(random_password(number, string.printable))} ")

print('')
for i in range(1, amount + 1):
    print(f"   Random String [Ascii Uppercase String]: {i} - {repr(random_password(number, string.ascii_uppercase))} ")
