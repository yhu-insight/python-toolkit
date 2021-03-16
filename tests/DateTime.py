# -*- coding: utf-8 -*-

# Python script to Process DateTime
# Author - HoneyMoose

import datetime

json_filename = 'resources/black_rock_test.json'

today = datetime.date.today()
print("Today's date:", today)

# Get date object from String
date_user = datetime.datetime.strptime('1/1/2021', '%m/%d/%Y')
print("Formatted DateTime ：", date_user)

# DateTime Object Output
print("DateTime Object Output 1 =", today.strftime("%d/%m/%Y"))
print("DateTime Object Output 2 =", today.strftime("%B %d, %Y"))
print("DateTime Object Output 3 =", today.strftime("%m/%d/%y"))
print("DateTime Object Output 4 =", today.strftime("%b-%d-%Y"))

# Current DateTime
now = datetime.datetime.now()
print("Current DateTime:", now)
