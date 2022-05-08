#Combining DataFrames
import pandas as pd
df1 = pd.DataFrame({'X': [15, 0], 'Y': [5, 5]})
df2 = pd.DataFrame({'X': [1, 1], 'Y': [4, 4]})
take_smaller = lambda s1, s2: s1 if s1.sum() < s2.sum() else s2
df1.combine(df2, take_smaller)
print(df1)