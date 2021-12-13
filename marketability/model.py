import pandas as pd

data = pd.read_csv('../product_info_list.csv')

data.drop(columns=['Unnamed: 0','product_title'],inplace=True)
data['period'] = data['total_sales'] / data['montly_sales']
data['period'] = data['period'].round(2)

import numpy as np
data['marketability'] = round((np.sqrt((data['favorites'] + data['ratings']) * data['star'] * data['total_sales'])) / data['period']).fillna(0)

#brand 제외
df = data[['lowest_price','discount_rate','weight','warranty','capacity','stock','power','marketability']]

import pickle

import sklearn
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

y = df.marketability
x = df[['lowest_price','discount_rate','weight','warranty','capacity','stock','power']]

pipe = Pipeline(steps=[
    ('preprocessor',SimpleImputer(strategy='median')), 
    ('model',RandomForestRegressor(max_depth = 10, n_jobs=-1, random_state=2))
])
k = 10

scores = -1* cross_val_score(pipe, x, y, cv=k, 
                         scoring='neg_mean_absolute_error')

model = pipe.fit(x.values,y)

pickle.dump(model, open('marketability.pkl','wb'))