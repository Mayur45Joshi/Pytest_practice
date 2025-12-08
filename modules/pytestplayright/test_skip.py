import pytest


@pytest.mark.skip
def test_loginfb(setup):
    print("login by fb")

@pytest.mark.regression
@pytest.mark.sanity
def test_loginx(setup):
    print("login by x")

@pytest.mark.skip
def test_loginln(setup):
    print("login by ln")

@pytest.mark.sanity
def test_signupfb(setup):
        print("signup by fb")

def test_signupx(setup):
        print("sign up by x")

@pytest.mark.sanity
def test_signupln(setup):
        print("sign up by ln")
