import pandas as pd


def test_1():
    df1 = pd.DataFrame({'name': ['xiao1', 'xiao2'], 'age': [18, 19]})
    df1.to_csv('data/1.csv')

    df2 = pd.read_csv('data/1.csv')
    # 取第二列开始以及后面的列
    df2 = df2.iloc[:, 1:]
    assert [0, 1] == df2.index.values.tolist() \
        and ['name', 'age'] == df2.columns.values.tolist() \
        and [['xiao1', 18], ['xiao2', 19]] == df2.values.tolist(), 'csv error'

    assert df1.values.tolist() == df2.values.tolist(), 'csv 2 error'
