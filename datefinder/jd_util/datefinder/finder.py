import re
from itertools import chain
from jd_util.datefinder.const import JD_DATES
from numpy import nan

class DateFinder(object):
    def __init__(self, config=None):
        pass
    def finditer(self, text):
        # split space
        if text is None or text is nan or not isinstance(text, str):
            return []
        iters = []
        for regex in JD_DATES:
            jd_regex = re.compile(regex)
            iters.append(jd_regex.finditer(text))
        return chain.from_iterable(iters)
