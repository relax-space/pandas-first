import pandas as pd


def test_1():
    # 排序
    df1 = pd.DataFrame([[1, 2, 3], [4, 2, 1]])
    df2 = df1.sort_index(ascending=False)
    assert [[4, 2, 1], [1, 2, 3]] == df2.values.tolist(), 'sort_index error'

    df3 = df1.sort_index(axis=1, ascending=False)
    assert [[3, 2, 1], [1, 2, 4]] == df3.values.tolist(), 'sort_index 2 error'


def test_2():
    # 查询
    df1 = pd.DataFrame([[1, 2, 3], [4, 2, 1]],columns=['A','B','C'])
    df1.query('A>1 and B>1',inplace=True)
    assert [4,2,1] == df1.iloc[0].values.tolist(),'query error'
    
    
    df1 = pd.DataFrame([[1,2,3],[4,2,100]])
    df2 = df1[df1[0].gt(1) & df1[1].gt(1)]
    assert [4,2,100] == df2.iloc[0].values.tolist(),'query error'
