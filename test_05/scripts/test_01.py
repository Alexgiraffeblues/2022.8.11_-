import sys, pytest
sys.path.insert(0, r'C:\Users\长颈鹿蓝调\Desktop\学习\黑马_软件测试\代码\Python学习代码\2022.8.11_考试')
from test_05.common.read_data import get_data

class Test:
    @pytest.mark.parametrize('name, school', get_data())
    def test_print_info(self, name, school):
        print(f'姓名：{name}, 学校名称：{school}')
    
    @pytest.mark.parametrize('name, school', get_data())
    def test_judge_name(self, name, school):
        assert '小明' == name
        print('姓名等于小明')
        assert '清华' in school
        print('学校名称包含清华')