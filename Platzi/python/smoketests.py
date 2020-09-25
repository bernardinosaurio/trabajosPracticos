from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTesT
from searchtest import Searchtest

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTesT)
search_test = TestLoader().loadTestFromTestCase(searchtests)

smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)