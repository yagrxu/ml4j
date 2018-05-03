
import unittest
from  jd_util.datefinder.finder import DateFinder

sample_incidents = [
    "Sunday, March 15-16.", 
    "Sunday, 3/15.", 
    "Sunday, March 15.", 
    "Sunday, Apr 15 and 16.", 
    "Sunday, Oct 1st,", 
    "Sunday, 10 of May."]


class Test(unittest.TestCase):

    def testName(self):
        df = DateFinder()
        for text in sample_incidents:
            print(text)
            for result in df.finditer(text):
                print((result.start(), result.group()[:-1]))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
