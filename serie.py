import numpy as np
import pandas as pd


def test_1():
    sr = pd.Series([1, 2, 3])
    assert np.ndarray == type(sr.values) and [
        1, 2, 3] == sr.values.tolist(), 'series value error'

    assert np.ndarray == type(sr.index.values) and [
        0, 1, 2] == sr.index.values.tolist(), 'series index error'


def test_2():
    # copy 跟asarray类似, 都是只有参数是ndarray,并且不改变dtype的时候,才会不复制.
    # 1. 复制: 参数为array不会改
    a1 = [1, 2, 3]
    sr = pd.Series(a1, copy=False)
    sr.iloc[0] = 100
    assert [1, 2, 3] == a1 and [
        100, 2, 3] == sr.values.tolist(), 'series copy error'
    # 2. 不复制: 参数为ndarray会改
    a2 = np.array([1, 2, 3])
    sr = pd.Series(a2, copy=False)
    sr.iloc[0] = 100
    assert [100, 2, 3] == a2.tolist() and [
        100, 2, 3] == sr.values.tolist(), 'series copy 2 error'
    # 3. 复制: 参数为ndarray,但是修改dtype 也不会改
    a3 = np.array([1, 2, 3])
    assert np.dtype('i4') == a3.dtype, 'series copy 3 error'
    sr = pd.Series(a3, dtype=np.dtype('i8'), copy=False)
    sr.iloc[0] = 100
    assert [1, 2, 3] == a3.tolist() and [
        100, 2, 3] == sr.values.tolist(), 'series copy 3 error'


def test_3():
    # index
    a1 = pd.Series(['xiao', 'xinmiao'], index=['x', 'y'])
    assert 'xinmiao' == a1['y'], 'series index error'

    a2 = pd.Series({'x': 10, 'y': 24})
    assert 24 == a2['y'], 'series index 2 error'
