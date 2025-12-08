import pytest

class TestClass:

    @pytest.fixture()  #decorators
    def setup(self):
        print("befor launching browser")
        print("before opem application")
        yield
        print("after test case")
    def test_login(self,setup):
        print("this is login method")
    def test_search(self,setup):
        print("this is search method")
    def test_advancesearch(self):
        print("this is advance search")

