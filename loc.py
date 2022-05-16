'''
说明: loc和iloc有几个功能
1. 可以获取一行或者多行数据
2. 可以获取1列或多列数据
3. 可以获取某个单元格的数据

对应dataframe来说, 在不指定index和columns的情况下,iloc和loc一样
区别在于,iloc根据索引下标取值, loc根据索引值取值
'''
import numpy as np
import pandas as pd


def test_1():
    # 按行取值
    pf = pd.DataFrame([[1, 2], [3, 4]])
    iloc_0 = pf.iloc[0]
    loc_0 = pf.loc[0]
    assert pd.Series == type(iloc_0) == type(loc_0), 'loc error'
    assert [1, 2
            ] == iloc_0.values.tolist() == loc_0.values.tolist(), 'loc 2 error'

    iloc_01 = pf.iloc[0:2]
    assert [[1, 2], [3, 4]] == iloc_01.values.tolist(), 'loc 3 error'


def test_2():
    # 按列取值
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
    iloc_0 = df.iloc[:, 0]
    loc_0 = df.loc[:, 0]
    assert pd.Series == type(iloc_0) == type(loc_0), 'loc2 1 error'
    assert [
        1, 4
    ] == iloc_0.values.tolist() == loc_0.values.tolist(), 'loc2 2 error'

    loc_01 = df.loc[:, 0:1]
    assert pd.DataFrame == type(loc_01), 'loc2 3 error'
    assert [[1, 2], [4, 5]] == loc_01.values.tolist(), 'loc2 4 error'


def test_3():
    # 按单元格取值
    df = pd.DataFrame([[1, 2], [3, 4]])
    iloc_00 = df.iloc[0, 0]
    loc_00 = df.loc[0, 0]
    assert np.int64 == type(iloc_00) == type(loc_00), 'loc3 1 error'
    assert 1.0 == iloc_00 == loc_00, 'loc3 2 error'


def test_4():
    # loc 和iloc 区别, 当设置index或columns参数后
    df = pd.DataFrame([[1, 2], [3, 4]],
                      index=['day1', 'day2'],
                      columns=['grape', 'pineapple'])
    # 第一行
    iloc_0 = df.iloc[0]
    loc_0 = df.loc['day1']
    assert [
        1, 2
    ] == iloc_0.values.tolist() == loc_0.values.tolist(), 'loc4 1 error'

    # 第一列
    iloc_col_0 = df.iloc[:, 0]
    loc_col_0 = df.loc[:, 'grape']
    assert [1, 3] == iloc_col_0.values.tolist() == loc_col_0.values.tolist(
    ), 'loc4 2 error'
