import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def total(df: pd.DataFrame):
    f, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 9))
    s0 = df['behavior_type'].value_counts()
    s0 = s0.reset_index()
    print(s0)
    p1 = sns.barplot(x=s0.index, y=s0.behavior_type, data=s0, ax=axes[0])
    p1.set_title('各环节人数对比图')
    p1.set_xlabel('用户行为')
    p1.set_ylabel('人数')

    s1 = df['behavior_type'].value_counts()
    s2 = s1 / s1.shift(1)
    s2 = s2.fillna(1)
    s2 = s2.reset_index()
    print(s2)
    p = sns.lineplot(x=s2.index, y=s2.behavior_type, data=s2, ax=axes[1])
    p.set_title('各环节转换率对比图')
    p.set_xlabel('用户行为')
    p.set_ylabel('转换率')


def product(df: pd.DataFrame):

    f, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 9))

    df3 = pd.pivot_table(data=df,
                         values='date',
                         index='behavior_type',
                         columns='item',
                         aggfunc='count')
    p = sns.lineplot(data=df3, ax=axes[0])
    p.set_title('各个商品不同环节人数对比图')
    p.set_xlabel('用户行为')
    p.set_ylabel('人数')

    s1 = df.groupby(['item', 'behavior_type']).count()['date']
    print(s1)
    s2 = s1 / s1.shift(1)
    s2 = s2.fillna(1)
    s2 = s2.reset_index()
    s2.loc[s2.query('behavior_type==0').index, 'date'] = 1
    print(s2)
    p2 = sns.lineplot(x=s2.behavior_type,
                      y=s2.date,
                      hue='item',
                      data=s2,
                      ax=axes[1])
    p2.set_title('各个商品不同环节转换率对比图')
    p2.set_xlabel('用户行为')
    p2.set_ylabel('转换率')


def main():
    sns.set_style({'font.sans-serif': 'Microsoft YaHei'})
    plt.rcParams['font.sans-serif'] = ['SimHei']
    df = pd.read_csv('asset/miao.csv')

    total(df)

    product(df)

    plt.show()

    pass


if __name__ == '__main__':
    main()
