# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 14:15:42 2022

@author: Rahul
"""

import pandas as pd
import numpy as np

df = pd.read_csv("D:\\DS\\books\\ASSIGNMENTS\\Recommendation System\\book.csv", encoding = 'latin-1')

df.drop(columns=('Unnamed: 0'),axis=1,inplace=True)
#dropping unrequired columns

df.rename(columns={'User.ID':'UserID',#renaming column names
                   "Book.Title":"BookTitle",
                   "Book.Rating":"BookRating"},inplace=True)

df.head()

df.info()

df.describe()

df.isnull().any()

len(df)
df.sort_values('UserID')
len(df.UserID.unique())

df.BookRating.value_counts().plot(kind='bar')

df['BookRating'].hist()

df.BookTitle.value_counts()

# Use Pivot Table to Reshape the Data
df1 = df.pivot_table(index = 'UserID', 
                     columns = 'BookTitle',
                     values = 'BookRating')
print(df1)

df1.fillna(0, inplace = True)
# Replaced null value with 0
df1

from sklearn.metrics import pairwise_distances
df2 = 1-pairwise_distances(df1.values,metric = 'cosine')
df2

df_1 = pd.DataFrame(df2)

# Set the index and Column names to user 
df_1.index = df.UserID.unique()
df_1.columns = df.UserID.unique()

df_1

df_1.iloc[:,:5]

np.fill_diagonal(df2, 0)
df_1.iloc[0:7, 0:7]


# To save your cosin calcutaion file
#df_1.to_csv("cosin_calc.csv")


# Most Similar Users
df_1.max()
df_1.idxmax(axis=1)[0:10]

df[(df['UserID'] == 276729) | (df['UserID'] == 276726)]

# System will recommend 'Classical Mythology' to 276729 and 'Decision in Normandy' & 'Clara Callan' to276726
user_1 = df[df['UserID'] == 276729]
user_2 = df[df['UserID']  == 276726]

pd.merge(user_1,user_2,on='BookTitle',how='inner')
pd.merge(user_1,user_2,on='BookTitle',how='outer')



df[(df['UserID'] == 276736) | (df['UserID'] == 276726)]
# System will recommend 'Classical Mythology' to 276736 and 'Flu: The Story of the Great Influenza Pandemic' to 276726
user_1 = df[df['UserID'] == 276736]
user_2 = df[df['UserID']  == 276726]

pd.merge(user_1,user_2,on='BookTitle', how='inner')
pd.merge(user_1,user_2,on='BookTitle',how='outer')



df[(df['UserID'] == 276744) | (df['UserID'] == 276726)]

# System will recommend 'Classical Mythology' to 276744 and 'The Kitchen God's Wife' & to276726
user_1 = df[df['UserID'] == 276744]
user_2 = df[df['UserID']  == 276726]

pd.merge(user_1,user_2,on='BookTitle', how='inner')
pd.merge(user_1,user_2,on='BookTitle',how='outer')



df[(df['UserID'] == 276754) | (df['UserID'] == 276726)]

# System will recommend 'Classical Mythology' to 276754 and 'A Second Chicken Soup for the Woman's Soul' to 276726
user_1 = df[df['UserID'] == 276754]
user_2 = df[df['UserID']  == 276726]

pd.merge(user_1,user_2,on='BookTitle', how='inner')
pd.merge(user_1,user_2,on='BookTitle',how='outer')



df[(df['UserID'] == 276745) | (df['UserID'] == 276726)]

# System will recommend 'Classical Mythology' to 276745 and 'What If?: The World's Foremost Military Histor' to 276726
user_1 = df[df['UserID'] == 276745]
user_2 = df[df['UserID']  == 276726]

pd.merge(user_1,user_2,on='BookTitle', how='inner')
pd.merge(user_1,user_2,on='BookTitle',how='outer')










