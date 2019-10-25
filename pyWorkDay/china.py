# -*- coding:utf-8 -*-
#
#
#
#
###
__author = "cgfANtUAN"

import chinaholiday

from datetime import datetime


#判断是不是holiday
def judgeHoliday(dateStr):
    dateTemp = datetime.strptime(dateStr, "%Y-%m-%d").year
    print dateTemp
    print chinaholiday.holidays[dateTemp]




if __name__ == "__main__":
    judgeHoliday("2019-09-29")