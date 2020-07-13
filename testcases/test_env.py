
def test_case(cmdoption):
    print("测试环境验证")
    env, data = cmdoption
    print(f"环境 ： {env} , 数据：{data}")
    ip = data['ip']
    port = data['port']
    url = 'http://' + str(ip) + ":" + str(port)
    # requests.get(url)
    print(url)