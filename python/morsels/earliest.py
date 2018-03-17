#!/usr/local/bin/python3

# days = {
#     "Jan": 31,
#     "Feb": 28,
#     "Mar": 31,
#     "Apr": 30,
#     "May": 31,
#     "Jun": 30,
#     "Jul": 31,
#     "Aug": 31,
#     "Sep": 30,
#     "Oct": 31,
#     "Nov": 30,
#     "Dec": 31
# }

days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def get_days(date_str):
    (d1_mm, d1_dd, d1_yy) = date_str.split('/')

    d1m = int(d1_mm)
    d1d = int(d1_dd)
    d1y = int(d1_yy)

    days_d1_mm = 0

    for month in days.keys():
        if (month < d1m):
            days_d1_mm = days_d1_mm + days[month]
        elif (month == d1m):
            if (d1d > days[month]):
                days_d1_mm = days_d1_mm + days[month]
            else:
                days_d1_mm = days_d1_mm + d1d

    total_days = days_d1_mm + d1y
    print (total_days)
    return (total_days)


def get_earliest(date1, date2):
    days_dict = {}

    days1 = get_days(date1)
    days_dict[days1] = date1

    days2 = get_days(date2)
    days_dict[days2] = date2

    #print (sorted(days_dict))
    for earliest in sorted(days_dict):
        print ("Earliest is {}".format(days_dict[earliest]))
        exit(0)


def main():
    date1 = input("Enter first date  : ")
    date2 = input("Enter second date : ")

    get_earliest(date1, date2)

if __name__ == "__main__":
    main()
