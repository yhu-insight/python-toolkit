# -*- coding: utf-8 -*-

# Python Random String Password
# Author - yucheng.hu@insight.com

import string
from random import choice


def random_password(length, printable):
    """
    Provides a random password of the given length.
    :param int length: The length of the password to generate.
    """

    return "".join([choice(printable) for x in range(int(length))])


if __name__ == "__main__":
    3

amount = int(input("How many passwords: "))
number = int(input("Length of password? "))

for i in range(1, amount + 1):
    print(f"   Password [Printable String]: {i} - {repr(random_password(number, string.printable))} ")

print('')
for i in range(1, amount + 1):
    print(f"   Password [Ascii Uppercase String]: {i} - {repr(random_password(number, string.ascii_uppercase))} ")
