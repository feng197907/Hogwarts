import pytest
import allure
import os

test_data = ([(1, 1, 2), (2, 2, 4), (4, 8, 9)], [(10, 1, 9), (12, 2, 10), (14, 8, 9)],
             [(3, 10, 30), (2, 8, 14), (4, 8, 30)], [(15, 3, 5), (20, 2, 10), (14, 7, 2)])


class Test_Pytest():

    @pytest.mark.parametrize('a,b,result', test_data[0])
    def test_add(self, fixture_func, a, b, result):
        assert fixture_func.add(a, b) == result

    @pytest.mark.parametrize('a,b,result', test_data[1])
    def test_sub(self, fixture_func, a, b, result):
        assert fixture_func.sub(a, b) == result

    @pytest.mark.parametrize('a,b,result', test_data[2])
    def test_mult(self, fixture_func, a, b, result):
        assert fixture_func.mult(a, b) == result

    @pytest.mark.parametrize('a,b,result', test_data[3])
    def test_div(self, fixture_func, a, b, result):
        assert fixture_func.div(a, b) == result


if __name__ == "__main__":
    pytest.main(["-s", "--alluredir", "./result", "test_func.py"])
    os.system('allure generate ./result -o ./report --clean')
