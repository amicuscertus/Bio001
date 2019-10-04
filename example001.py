import numpy as np
import pandas as pd
import seaborn as sns
 
df = pd.read_csv('http://academia.rdy.jp/bioinf/wp-content/uploads/2019/05/Subjectdata.csv')
df.describe()
 
df.isnull().sum()
 
df["Height"].plot()
df["Weight"].plot()
df["Therapeutic Dose of Warfarin"].plot()
 
df = df.loc[:, ["Therapeutic Dose of Warfarin", "Height", "Weight", "Gender", "Age"]]
df.describe()
 
df.tail(2)
 
df.isnull().sum()
 
df.dropna(inplace=True)
df.isnull().sum()
 
df["Height"].plot()
df["Weight"].plot()
df["Therapeutic Dose of Warfarin"].plot()
 
df.tail(2)
 
df.describe()
 
df.reset_index(inplace=True)
df.tail()
 
df["Height"].plot()
df["Weight"].plot()
df["Therapeutic Dose of Warfarin"].plot()
 
sns.pairplot(df[["Height", "Weight", "Therapeutic Dose of Warfarin"]], diag_kind="kde")
 
sns.distplot(df["Height"])
sns.distplot(df["Weight"])
sns.distplot(df["Therapeutic Dose of Warfarin"])
 
df.columns
 
df.rename(columns={'Height':'H', 'Weight':'W'}, inplace=True)
 df.head(2)
 
df['Age'].unique()
 
df[['a', 'b']] = df['Age'].str.split('0',expand=True)
df.head(2)
 
df['age'] = df['a'].astype(int) * 10 + 5
df.head(2)
 
df.describe()
 
df['age'].hist(bins=40)
 
sns.distplot(df['age'])
