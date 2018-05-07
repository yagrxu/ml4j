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

``` python
import jd_util.datefinder as finder
# the output below is an array
print(finder.find('a date 10th May here'))

```