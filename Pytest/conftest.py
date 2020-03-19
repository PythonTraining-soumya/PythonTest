# if you think that the fixture is common to all the pytest test files in the test folder then declare that fixture in
# conftest so that that fixture wil be available to all the pytest test files available in that test folder
# it is mandatory to give the file name as conftest.py
# add argument in pytest.fixture as scope="class" so that the before and after methods will get executed only once


import pytest


@pytest.fixture(scope="class")
def test_setup():
    print("Will be executed first")
    yield
    print("will get executed after the execution of all the test cases")


@pytest.fixture()
def test_loadData():
    print("all the data's are loaded")
    return ["Soumya", "31", "Married"]


@pytest.fixture(params=[("Chrome", "soumya", "31"), ("Firefox", "Balu", "35"), "IE"])  # this is how w e can send
# multiple value in a single run
def test_crossBrowser(request):  # use request which is connected to fixtures only when there is argument in the fixture
    return request.param
