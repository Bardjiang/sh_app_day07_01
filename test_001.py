# import allure
#
# class Test_001():
#
#     @allure.step(title="这是一个登陆方法")
#     def test_login(self):
#         allure.attach("desc","username")
#         allure.attach("desc", "username")
#         assert 1
#
#     @allure.step(title = "这是一个订单方法")
#     def test_order(self):
#         assert 0
#
#     def test_quit(self):
#         assert 1\\


import allure,pytest

class Test_001():

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="login")
    def test_001(self):
        allure.attach("step1","初始化登陆")
        allure.attach("step1", "输入用户名")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="ordering")
    def test_002(self):
        allure.attach("desc","购物")
        assert 0