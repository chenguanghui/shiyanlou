#!/usr/bin/env python3

import sys

try:
    # ????????????
    ynssde = int(sys.argv[1]) - 3500
    ynse = 0
    # ??????
    if ynssde <= 0:
        print(format(0, ".2f"))
    elif ynssde > 0 and ynssde <= 1500:
        ynse = ynssde * 0.03 - 0
        print(format(ynse, ".2f"))
    elif ynssde > 1500 and ynssde <= 4500:
        ynse = ynssde * 0.10 - 105
        print(format(ynse, ".2f"))
    elif ynssde > 4500 and ynssde <= 9000:
        ynse = ynssde * 0.20 - 555
        print(format(ynse, ".2f"))
    elif ynssde > 9000 and ynssde <= 35000:
        ynse = ynssde * 0.25 - 1005
        print(format(ynse, ".2f"))
    elif ynssde > 35000 and ynssde <= 55000:
        ynse = ynssde * 0.30 - 2755
        print(format(ynse, ".2f"))
    elif ynssde > 55000 and ynssde <= 80000:
        ynse = ynssde * 0.35 - 5505
        print(format(ynse, ".2f"))
    else:
        ynse = ynssde * 0.45 - 13505
        print(format(ynse, ".2f"))
except:
    print("Parameter Error")
