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
import jd_util.datefinder as finder
# code: the output below is an array
print(finder.find('a date 10th May here'))

```