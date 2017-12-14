#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

employeedict = {}
employee_aftertax = {}

for arg in sys.argv[1:]:
    try:
        dictinfo = arg.split(":")
        employeedict[dictinfo[0]] = int(dictinfo[1])
        # print(employeedict[int(dictinfo[0])])
    except ValueError:
        print("Parameter Error")
        exit()

def aftertax(employeedict):
    afteremployeedict = {}
    for key,value in employeedict.items():
        ynssde = value * (1 - 0.08 - 0.02 - 0.005 - 0.00 - 0.00 - 0.06) - 3500

        if ynssde <= 0:
            result = 0.00
        elif 0 < ynssde <= 1500:
            result = ynssde * 0.03 - 0
        elif 1500 < ynssde <= 4500:
            result = ynssde * 0.1 - 105
        elif 4500 < ynssde <= 9000:
            result = ynssde * 0.2 - 555
        elif 9000 < ynssde <= 35000:
            result = ynssde * 0.25 - 1005
        elif 35000 < ynssde <= 55000:
            result = ynssde * 0.3 - 2755
        elif 55000 < ynssde <= 80000:
            result = ynssde * 0.35 - 5505
        else:
            result = ynssde * 0.45 - 13505

        employee_aftertax[key] = value * (1 - 0.08 - 0.02 - 0.005 - 0.00 - 0.00 - 0.06) - result
    return employee_aftertax


if __name__ == "__main__":
    employee_aftertax = aftertax(employeedict)
    for key,value in employee_aftertax.items():
        print(key + ':' + str(format(value, '.2f')))
        # print(key, format(value, ".2f"))
