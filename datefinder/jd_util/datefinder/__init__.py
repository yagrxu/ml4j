from jd_util.datefinder.finder import  DateFinder
finder = None

def find(text, config=None):
    global finder
    if finder is None:
        finder = DateFinder()
    iterator = finder.finditer(text)
    my_map = {}
    for item in iterator:
        _key = str(item.start())
        if _key in my_map and len(my_map[_key]) < len(item.group()):
            my_map[_key] = item.group()
        else:
            my_map[_key] = item.group()
    ret = []
    
    for key in my_map:
        ret.append(my_map[key][:-1]) # remove last char as it is the indication for closing
    return ret