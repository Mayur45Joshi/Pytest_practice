# import pytest
#
#
# @pytest.mark.order(2)
# def test_loginfb(setup):
#     print("login by fb")
#
# @pytest.mark.order(3)
# def test_loginx(setup):
#     print("login by x")
#
# @pytest.mark.order(1)
# def test_loginln(setup):
#     print("login by ln")


##########################################################

# Approach 2: using before , after
# import pytest
#
# @pytest.mark.order(1)
# def test_login():
#     print("this is login test")
#
# @pytest.mark.order(before="test_checkout")
# def test_add_item():
#     print("this is add item test")
#
# @pytest.mark.order(after="test_add_item")
# def test_checkout():
#     print("this is checkout")

###################################################################

# Approach 3: using marker string ( user defined)
import pytest

@pytest.mark.order("last")
def test_checkout():
    print("this is ckeckout")

@pytest.mark.order()
def test_add_item():
    print("this is add item test")

@pytest.mark.order("first")
def test_login():
    print("this is login")