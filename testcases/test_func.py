import pytest
import allure
import os


class Test_Pytest():

    @pytest.mark.parametrize('a,b,result', [(1, 1, 2), (2, 2, 4), (4, 8, 9)])
    def test_add(self, cal_demo, a, b, result):
        assert cal_demo.add(a, b) == result

    @pytest.mark.parametrize('a,b,result', [(10, 1, 9), (12, 2, 10), (14, 8, 9)])
    def test_sub(self, cal_demo, a, b, result):
        assert cal_demo.sub(a, b) == result

    @pytest.mark.parametrize('a,b,result', [(3, 10, 30), (2, 8, 14), (4, 8, 30)])
    def test_mult(self, cal_demo, a, b, result):
        assert cal_demo.mult(a, b) == result

    @pytest.mark.parametrize('a,b,result', [(15, 3, 5), (20, 2, 10), (14, 7, 2)])
    def test_div(self, cal_demo, a, b, result):
        assert cal_demo.div(a, b) == result


if __name__ == "__main__":
    pytest.main(["-s", "--alluredir", "./result", "test_func.py"])
    os.system('allure generate ./result -o ./report --clean')
