import pytest
import allure
import os
import yaml

with open('../datas/calc.yaml') as f:
    datas = yaml.safe_load(f)
    myids, mydatas = {}, {}
    for key, data in datas.items():
        myids[key] = data.keys()
        mydatas[key] = data.values()


def test_div(param1):
    print(f"param = {param1[0]}")
    print("动态生成测试用例")


class Test_Pytest():

    # @pytest.mark.last
    # @pytest.mark.parametrize('a,b,result', divdatas, ids=divids)
    # @pytest.mark.dependency(depends=["Test_Pytest::test_mult"])
    @allure.feature('除法测试')
    def test_div(self, fixture_func, param1):
        assert fixture_func.div(param1[0], param1[1]) == param1[2]

    # @pytest.mark.run(order=3)
    # @pytest.mark.parametrize('a,b,result', multdatas, ids=multids)
    # @pytest.mark.dependency()
    @allure.feature('乘法测试')
    def test_mult(self, fixture_func, param1):
        assert fixture_func.mult(param1[0], param1[1]) == param1[2]
    #
    # @pytest.mark.run(order=1)
    # @pytest.mark.parametrize('a,b,result', adddatas, ids=addids)
    # @pytest.mark.dependency()
    @allure.feature('加法测试')
    def test_add(self, fixture_func, param1):
        assert fixture_func.add(param1[0], param1[1]) == param1[2]
    #
    # @pytest.mark.run(order=2)
    # @pytest.mark.parametrize('a,b,result', subdatas, ids=subids)
    # @pytest.mark.dependency(depends=["Test_Pytest::test_add"])
    @allure.feature('减法测试')
    def test_sub(self, fixture_func, param1):
        assert fixture_func.sub(param1[0], param1[1]) == param1[2]




if __name__ == "__main__":
    pytest.main(["-s", "--alluredir", "./result", "test_func.py"])
    os.system('allure generate ./result -o ./report --clean')
    # ope_fun()
