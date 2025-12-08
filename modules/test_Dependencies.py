import pytest

class Testclass:

    @pytest.mark.dependency()
    def test_openApp(self):
        assert True

    @pytest.mark.dependency(depends=['Testclass::test_openApp'])
    def test_login(self):
        assert False

    @pytest.mark.dependency(depends=['Testclass::test_login'])
    def test_search(self):
        assert True

    @pytest.mark.dependency(depends=['Testclass::test_login','Testclass::test_search'])
    def test_advSearch(self):
        assert True

    @pytest.mark.dependency(depends=['Testclass::test_login'])
    def test_logout(self):
        assert True
