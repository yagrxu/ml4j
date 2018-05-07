
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
MONTHS_NUM = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
BREV_MONTHS = [i[0:3] for i in MONTHS]
DATE_ENDS = '(,|\.|\s)'
NUMBERS = [str(i) for i in range(1, 32)]
ORD_NUMBERS = [
    str(x) + 'st' if str(x).endswith('1') 
    else (str(x) + 'nd' if str(x).endswith('2') 
          else (str(x) + 'rd' if str(x).endswith('3') 
                else (str(x) + 'th')
                )
          ) for x in  range(1, 32)]


def _from_to(my_list):
    ret = []
    for i in range(len(my_list)):
        for j in my_list[:i]:
            ret.append(j + "-" + my_list[i])
            ret.append(j + "\sand\s" + my_list[i])
    return ret


DAYS_BETWEEN = _from_to(NUMBERS) + _from_to(ORD_NUMBERS)
MONTH_REGEX = '|'.join(['(' + x + ')' for x in (MONTHS + MONTHS_NUM + BREV_MONTHS)])
DAY_REGEX = '|'.join(NUMBERS + ORD_NUMBERS)
DAYS_BETWEEN_REGEX = '|'.join(DAYS_BETWEEN)

JD_DATES = ['(' + MONTH_REGEX + ')(/|\s)(' + DAY_REGEX + ')' + DATE_ENDS,
            '(' + DAY_REGEX + ')((\sof\s)|\s)(' + MONTH_REGEX + ')' + DATE_ENDS,
            '(' + MONTH_REGEX + ')(/|\s)(' + DAYS_BETWEEN_REGEX + ')' + DATE_ENDS,
            '(' + DAYS_BETWEEN_REGEX + ')((\sof\s)|\s)(' + MONTH_REGEX + ')' + DATE_ENDS]
