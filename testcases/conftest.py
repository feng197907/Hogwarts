from typing import List

import pytest
from pyCode import calc
import yaml


@pytest.fixture()
def cal_demo():
    c = calc.Calculator()
    return c


@pytest.fixture()
def fixture_func(cal_demo):
    print("开始计算")
    yield cal_demo
    print("结束计算")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    print(len(items))
    # 倒序执行 items里面的测试用例
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        # if 'add' in item.nodeid:
        #     item.add_marker(pytest.mark.add)
        #
        # if 'div' in item.nodeid:
        #     item.add_marker(pytest.mark.div)


# 通过 方法动态的生成测试用例
def pytest_generate_tests(metafunc: "Metafunc") -> None:
    name = metafunc.function.__name__  # 获取当前case名
    if "param1" in metafunc.fixturenames and name in metafunc.module.mydatas.keys():
        metafunc.parametrize("param1",
                             metafunc.module.mydatas.get(name),  # 根据当前case名获取对应的数据
                             ids=metafunc.module.myids.get(name),
                             scope='function')

def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    with open('../datas/env.yaml') as f:
        datas = yaml.safe_load(f)

        if myenv == 'test':
            data = datas['test']
        elif myenv == 'dev':
            data = datas['div']
        else:
            data = datas['st']

    return myenv, data
