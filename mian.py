import unittest
import HTMLTestRunnerNew
from testcases import test_login
from testcases import test_recharge

su = unittest.TestSuite()
loder = unittest.TestLoader()
su.addTest(loder.loadTestsFromModule(test_login))
su.addTest(loder.loadTestsFromModule(test_recharge))

with open("api.html", "wb+") as file:
    test_run=HTMLTestRunnerNew.HTMLTestRunner(file,verbosity=2,title=None,description=None,tester=None)
    test_run.run(su)