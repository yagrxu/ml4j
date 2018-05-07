
import unittest
from  jd_util.datefinder.finder import DateFinder
import jd_util.datefinder as finder

sample_incidents = [
    ("Sunday, March 15-16.", 8, 1), 
    ("Sunday, 3/15.", 8, 1),  
    ("Sunday, March 15.", 8, 1), 
    ("Sunday, Apr 15 and 16.", 8, 1), 
    ("Sunday, Oct 1st,", 8, 1),  
    ("Sunday, 10 of May.", 8, 1),
    ("Sunday, on 9 of May we went to Xiaobaobao jia", 8, 1)  ]


class Test(unittest.TestCase):

    def test01(self):
        output = []
        for (text, unused_start_position, num) in sample_incidents:
            ret = finder.find(text)
            self.assertEqual(len(ret), num)
            output.append(ret)
        print(output)
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
