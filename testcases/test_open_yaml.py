import yaml
import pytest
# with open('../datas/env.yaml') as f:
#     datas = yaml.safe_load(f)
#     print(datas['test']["ip"])


def test_demo(request):
    myenv = request.config.getoption("--env")
    print(myenv+"--------")