# pandas-first

## 常用

- pd.merge(left, right, on="key")
- df.groupby("A").sum()
- df.groupby(["A", "B"]).sum()
- index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
- 透视表:pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])

## 性能

1.如果所有列有不同的类型, DataFrame.to_numpy()这个方法会耗性能
2.不要用pd.concat 添加行

## 引用

https://www.runoob.com/pandas/pandas-tutorial.html

https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
