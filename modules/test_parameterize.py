import pytest

class Testclass:

    @pytest.mark.parametrize('num1,num2',[(1,1),(3,5),(10,10),(7,8)])
    def test_calculator(self,num1,num2):
        assert num1==num2