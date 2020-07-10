import pytest
from pyCode import calc


@pytest.fixture(scope="function", autouse=True)
def fixture_func():
    print("开始计算")
    yield
    print("结束计算")


@pytest.fixture()
def cal_demo():
    c = calc.Calculator()
    return c
