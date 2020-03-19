# we are forced to add the fixture name as argument though you have declared globally when we have to return any
# value from the fixture

import pytest

from Pytest.Base import BaseClass


@pytest.mark.usefixtures("test_loadData")
class TestExample2Impl(BaseClass):
    def test_getData(self, test_loadData):
        log = self.test_getLogger()
        log.info(test_loadData)
        log.info(test_loadData[0: 2])
        log.info(test_loadData[0])
        print(test_loadData)
        print(test_loadData[0])
        print(test_loadData[0: 2])  # will print the 0th and the first index values
