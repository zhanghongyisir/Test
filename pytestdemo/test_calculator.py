import pytest
import yaml

from Calculator import Calculator


class TestCalculator:

    def setup_class(self):
        '''
        调用测试方法前输出【开始计算】
        :return:
        '''
        self.cal = Calculator()
        print("【开始计算】")

    def teardown_class(self):
        '''
        调用测试方法后输出【结束计算】
        :return:
        '''
        print("【结束计算】")

    @pytest.mark.parametrize('a,b,ex', yaml.safe_load(open("add_data.yaml")))
    def test_add(self, a, b, ex):
        '''
        加法校验用例
        :param a: 加数
        :param b: 加数
        :param ex: 期望值
        :return:
        '''
        assert ex == self.cal.add(a, b)

    @pytest.mark.parametrize('a,b,ex', yaml.safe_load(open("div_data.yaml")))
    def test_div(self, a, b, ex):
        '''
        除法校验用例
        :param a: 被除数
        :param b:除数
        :param ex:期望值
        :return:
        '''
        assert ex == self.cal.div(a, b)


if __name__ == '__main__':
    pytest.main(['-v'])

