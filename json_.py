import pandas as pd
from glom import glom

data = {
    'school': '中国大学',
    'info': {
        'address': '中国',
        'contact': {
            'tel': '123456789',
            'email': '123@china.com'
        }
    },
    'students': [
        {
            'id': 1,
            'name': '刘德华'
        },
        {
            'id': 2,
            'name': '张学友'
        }
    ]
}


def test_1():
    # 用json_normalize 提取复杂结构中的数据
    df1 = pd.json_normalize(data, record_path=['students'], meta=[
                            'school', ['info', 'contact', 'tel']])
    assert [0, 1] == df1.index.values.tolist() \
        and ['id', 'name', 'school', 'info.contact.tel'] == df1.columns.values.tolist() \
        and [[1, '刘德华', '中国大学', '123456789'], [2, '张学友', '中国大学', '123456789']] == df1.values.tolist(), 'json_normalize error'


def test_2():

    # 提取简单数据, 其实不太会用
    sr1 = pd.Series([{'id': 1, 'name': 'liu'}, {'id': 2, 'name': 'zhang'}])
    res = sr1.apply(lambda row: glom(row, {'name': 'name'}))
    print(type(res), res)
