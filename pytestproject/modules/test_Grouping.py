import pytest

class Testclass:

    @pytest.mark.sanity
    def test_loginByEmail(self):
        print("this is login by email")
        assert True==True

    @pytest.mark.reg
    def test_loginByFB(self):
        print("login by fb")
        assert True==True

    @pytest.mark.reg
    @pytest.mark.sanity
    def test_loginByTwitter(self):
        print("login by twitter")
        assert True==True

    @pytest.mark.reg
    @pytest.mark.sanity
    def test_signupByEmail(self,setup):
        print("this is signup by email")
        assert True == True

    @pytest.mark.sanity
    def test_signupByFB(self,setup):
        print("signup by fb")
        assert True == True

    @pytest.mark.reg
    def test_signupByTwitter(self,setup):
        print("signup by twitter")
        assert True == True