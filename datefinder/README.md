# How to use it
## Packaging
```
python setup.py sdist --format=gztar
```

## Installation

```
pip install /your/path/to/the/.tar.gz
```

## How to use it

``` python

# import part
from jd_util.datefinder.finder import DateFinder


# code
finder = DateFinder()
iterator = finder.finditer("Sunday, March 15-16.")
for item in iterator:
	print(item.group())

```