import pytest
from pyCode import calc


@pytest.fixture()
def cal_demo():
    c = calc.Calculator()
    return c

@pytest.fixture()
def fixture_func(cal_demo):
    print("开始计算")
    yield cal_demo
    print("结束计算")



