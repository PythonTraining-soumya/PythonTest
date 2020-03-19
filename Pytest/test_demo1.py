# pytest is the testing framework in python to install pytest , open cmd and give the command pip install pytest to
# check the version of the pytest open cmd and give the command pytest --version to name any file in the pytest start
# with test_filename or end with _test in pytest whatever code you write in pytest framework , have to be written in
# pytest standards that is it must be inside the function pytest method name should always start with test keyword in
# python every method is treated as a test case to run  all the test cases in all clasees  in the pytest in cmd first
# copy the path of the pytest package  and put cd in cmd and paste it in cmd after that to run all the test use the
# command py.test use py.test -v the console output in test use py.test -v -s to see the correct output testcase name
# in python is nothing but the method name if you want to run the test cases in on pytest class the after copying the
# path and pasting it in the cmd after cd write the test file name and -v -s if you want to run only selected test
# cases from different files then use the below method copy the path of the pytest package and write after cd and
# write py.test -k commonmethodname -v -s -k stands for method name execution, -v stands for more info metadata,
# -s stands for logs in output if you want to identify only the test cases which are smoke or regression then how can
# we do it see below this is done by using the mark concept ie put @pytest.mark.smoke or @pytest.mark.regression on
# top of the test cases selected and in cmd use this command py.test -m smoke/regression -v -s
# when you declare any method in a class add the parameter self as argument to each method in the class
import pytest


@pytest.mark.usefixtures("test_setup")
class Test:
    def test_execution(self):
        print("successfully execute the tests")

    def test_firstProgram(self):
        print("HELLO WORLD!")

    def test_checkingName(self):
        print("The name is Soumya")

    @pytest.mark.smoke
    def test_loginPageLogin(self):
        print("Login page is successfully loaded")
