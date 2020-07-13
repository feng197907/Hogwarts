import pytest
import allure
import os
import yaml


with open("../datas/calc.yaml") as f:
    datas = yaml.safe_load(f)

    adddatas = datas['add'].values()
    addids = datas['add'].keys()

    subdatas = datas['sub'].values()
    subids = datas['sub'].keys()

    multdatas = datas['mult'].values()
    multids = datas['mult'].keys()

    divdatas = datas['div'].values()
    divids = datas['div'].keys()



    # mydatas = datas.values()
    # myids = datas.keys()

# def test_param(param1):
#     print(f"param = {param1}{mydatas}{myids}")
#     print("动态生成测试用例")


class Test_Pytest():

    @pytest.mark.last
    @pytest.mark.parametrize('a,b,result', divdatas, ids=divids)
    @pytest.mark.dependency(depends=["Test_Pytest::test_mult"])
    @allure.feature('除法测试')
    def check_div(self, fixture_func, a, b, result):
        assert fixture_func.div(a, b) == result

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,result', multdatas, ids=multids)
    @pytest.mark.dependency()
    @allure.feature('乘法测试')
    def test_mult(self, fixture_func, a, b, result):
        assert fixture_func.mult(a, b) == result

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,result', adddatas, ids=addids)
    @pytest.mark.dependency()
    @allure.feature('加法测试')
    def test_add(self, fixture_func, a, b, result):
        assert fixture_func.add(a, b) == result

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,result', subdatas, ids=subids)
    @pytest.mark.dependency(depends=["Test_Pytest::test_add"])
    @allure.feature('减法测试')
    def check_sub(self, fixture_func, a, b, result):
        assert fixture_func.sub(a, b) == result





if __name__ == "__main__":
    pytest.main(["-s", "--alluredir", "./result", "test_func.py"])
    os.system('allure generate ./result -o ./report --clean')
