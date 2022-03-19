import pandas as pd
from numpy import NaN

data = {
    'A': ['na', NaN, '', '--', 'good']
}


def test_1():
    # isnull 测试
    df1 = pd.DataFrame(data)
    v_null = df1['A'].isnull()
    assert [False, True, False, False,
            False] == v_null.values.tolist(), 'isnull error'


def test_2():
    # replace
    df1 = pd.DataFrame(data)
    df1.fillna(0, inplace=True)
    df1.replace({'--': '', 'na': 0}, inplace=True)

    df2 = df1['A']
    assert [0, 0, '', '', 'good'] == df2.values.tolist(), 'fillna error'


def test_3():
    # 清洗1: 错误日期
    df1 = pd.DataFrame(['2020-01-1', '2020-02', '2020/03', '20201011'])
    # 转换成字符格式
    # format="%Y-%d-%m %H:%M:%S"
    df1[0] = pd.to_datetime(df1[0]).apply(lambda x: x.strftime('%Y-%m-%d'))
    assert ['2020-01-01', '2020-02-01', '2020-03-01',
            '2020-10-11'] == df1[0].values.tolist(), 'to_datetime error'


def test_4():
    # 清洗2: 错误的年龄
    df1 = pd.DataFrame([1, 18, 500])

    for i in df1.index:
        if df1.loc[i, 0] >= 120:
            df1.loc[i, 0] = 120

    assert [1, 18, 120] == df1[0].values.tolist(), 'age error'


def test_5():
    # 清洗3: 重复数据
    df1 = pd.DataFrame([['a',1],['b',2],['c',3],['b',2]])
    
    df1.drop_duplicates(inplace=True)
    print(df1)
    
    assert [['a',1],['b',2],['c',3]]== df1.values.tolist(),'duplicate error'
