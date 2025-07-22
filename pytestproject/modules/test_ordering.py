# import pytest
#
# class Testclass:
#
#     @pytest.mark.third
#     def test_methodC(self):
#         print("C Method")
#
#     @pytest.mark.fourth
#     def test_methodD(self):
#         print("D Method")
#
#     @pytest.mark.first
#     def test_methodA(self):
#         print("A Method")
#
#     @pytest.mark.second
#     def test_methodB(self):
#         print("B Method")
#
#     @pytest.mark.fifth
#     def test_methodE(self):
#         print("E Method")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import pytest

class Testclass:

    @pytest.mark.run(order=3)
    def test_methodC(self):
        print("C Method")

    @pytest.mark.run(order=4)
    def test_methodD(self):
        print("D Method")

    @pytest.mark.run(order=1)
    def test_methodA(self):
        print("A Method")

    @pytest.mark.run(order=2)
    def test_methodB(self):
        print("B Method")

    @pytest.mark.run(order=5)
    def test_methodE(self):
        print("E Method")