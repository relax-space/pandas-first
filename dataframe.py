

import numpy as np
import pandas as pd


def test_1():
    # 列几种形式
    # 1.不写默认为0开始
    df1 = pd.DataFrame(['x', 'y'])
    assert [0] == df1.columns.values.tolist(
    ) and [0, 1] == df1.index.values.tolist(), 'df error'
    # 为什么值会是这个呢, 因为dataframe是一个二维数组,所以会自动将1维广播成2维
    assert [['x'], ['y']] == df1.values.tolist(), 'df 2 error'

    # 2.指定列名
    df2 = pd.DataFrame(['x', 'y'], columns=['第一列'])
    assert ['第一列'] == df2.columns.values.tolist(
    ) and [0, 1] == df2.index.values.tolist(), 'df 3 error'

    assert [['x'], ['y']] == df1.values.tolist(), 'df 4 error'

    # 3.字典格式1
    df3 = pd.DataFrame({'1c': [1, 2], '2c': [3, 4]})
    assert ['1c', '2c'] == df3.columns.values.tolist(), 'df 5 error'

    assert [[1, 3], [2, 4]] == df3.values.tolist(), 'df 6 error'

    # 4.字典格式2
    df4 = pd.DataFrame(
        [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}])
    assert ['a', 'b', 'c', 'd'] == df4.columns.values.tolist(), 'df 7 error'

    # 先替换nan为0,然后再转换成整数
    df4 = df4.fillna(0).astype(np.int32)
    assert [[1, 2, 0, 0], [0, 0, 3, 4]
            ] == df4.values.tolist(), 'df 8 error'


def test_2():
    # 根据行取值
    df1 = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['c1', 'c2'])
    sr1 = df1.loc[0]
    assert pd.Series == type(sr1) and [1, 2] == sr1.values.tolist() and [
        'c1', 'c2'] == sr1.index.values.tolist(), 'df loc error'

    sr2 = df1.loc[[0, 1]]
    assert pd.DataFrame == type(sr2) and [[1, 2], [3, 4]] == sr2.values.tolist() and [
        0, 1] == sr2.index.values.tolist() and ['c1', 'c2'] == sr2.columns.values.tolist(), 'df loc 2 error'


def test_3():
    # 按列取值
    df1 = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['c1', 'c2', 'c3'])
    sr1 = df1['c1']
    assert pd.Series == type(sr1) and [0, 1] == sr1.index.values.tolist() and [
        1, 4] == sr1.values.tolist(), 'df col error'

    sr2 = df1[['c1', 'c2']]
    assert pd.DataFrame == type(sr2) and [0, 1] == sr2.index.values.tolist() and [
        [1, 2], [4, 5]] == sr2.values.tolist(), 'df col error'
