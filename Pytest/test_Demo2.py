# if you want to run all the test cases except one may be if you are suspecting a failure or bug in that test case we
# can do it by @pytest.mark.skip on top of the particular test which you don't want to run or skip and in cmd just
# run all the test cases . @pytest.mark.xfail can be used if you think that a particular test case is required for
# further actions but dont want to get reported fixtures - are the methods in pytest which is used as prerequisite
# and post request in running a test (just as @BeforeTest and @AfterTest in TestNG) for that use the command below
# @pytest.fixture and below that write the method and after that where you have to depend on this fixture give the
# fiture method name as argument to that method which you need to execute before test if you want to write a method
# to execute after the test excecution is completed the use the yield keyword write the yield keyword below the
# fixture method test cases  and write the test case to be executed after the excecution after yield keyword
# data driven and parameterization can be done in fixtures with return statement in list format
# if you want to install pytest-html use the command pip install pytest-html
# if you want to get the html report use the code py.test --html=report.html to get the report of all the pytest files
# if you want to get the report of a specific file the use py.test filename --html=report.html


import pytest


@pytest.mark.skip
def test_checkingTest():
    msg = "Good Morning"
    assert msg == "hello", "the assertion is false as the strings don't match"


@pytest.mark.smoke
def test_loginPageLogout():
    print("logged out successfully")


@pytest.mark.xfail
def test_addition():
    a = 2
    b = 4
    assert a + 2 == b, "The assertion is correct"


def test_crossBrowserTest(test_crossBrowser):
    print(test_crossBrowser)
    print(test_crossBrowser[0: 3])
    print(test_crossBrowser[1])
