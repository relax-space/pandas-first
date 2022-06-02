import numpy as np
import pandas as pd


def get_data():
    return [
        {
            'user_id': 2,
            'price': np.nan,
            'year': '2020',
            'hour': '1'
        },
        {
            'user_id': 2,
            'price': 30,
            'year': '2020',
            'hour': '3',
        },
        {
            'user_id': 3,
            'price': 20,
            'year': '2021',
            'hour': '2',
        },
    ]


def test_1():
    d1 = get_data()
    df = pd.DataFrame(d1)
    s1 = df.groupby('year').count()['user_id']
    assert ['2020','2021'] == s1.index.values.tolist() \
        and [2,1] == s1.values.tolist() \
        and 'user_id'== s1.name, 'count error'

    s2 = df.groupby('year').nunique()['user_id']
    assert ['2020','2021'] == s2.index.values.tolist() \
        and [1,1] == s2.values.tolist() \
        and 'user_id'== s2.name, 'nunique error'

    s3 = df.groupby('year').sum()['user_id']
    assert ['2020','2021'] == s3.index.values.tolist() \
        and [4,3] == s3.values.tolist() \
        and 'user_id'== s3.name, 'nunique error'


def test_2():
    '''
    主要对比count 和 value_counts的区别, 当有price为nan的时候, 就会有区别
    '''
    df = pd.DataFrame(get_data())
    s1 = df.groupby('year').count()['price']
    assert [1, 1] == s1.values.tolist(), 'count error'
    s2 = df['year'].value_counts()
    assert [2, 1] == s2.values.tolist(), 'value_counts error'
