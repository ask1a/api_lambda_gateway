import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.externals import joblib
from sklearn.metrics import r2_score

import zipfile

# IMPORT

df = pd.read_csv('price_paid_records.csv', low_memory=True)

# Selection variables

df = df[['Price', 'Property Type', 'Old/New', 'Duration']]

# Compte des modalités

print(df['Property Type'].value_counts())
print(df['Old/New'].value_counts())
print(df['Duration'].value_counts())

# Train/test

y = df['Price']
X = df.drop('Price', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=11)

# Preprocessing

cat_featuress = ['Property Type', 'Old/New', 'Duration']
cat_feat_processer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))]
)

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', cat_feat_processer, cat_featuress)])

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', ElasticNet(random_state=rand_seed))
    ]
)

model.fit(X_train, y_train)
preds = model.predict(X_test)

# Enregistrement du modele

joblib.dump(model, 'house_price_model.pkl')

# Zip du modele pour etre pris en charge dans lambda
zipfile.ZipFile('model.zip', mode='w').write("house_price_model.pkl")
