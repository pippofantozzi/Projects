import pandas as pd

dataset = pd.read_csv('life_expectancy.csv')
dataset = dataset.drop(columns = ['Country'],axis = 1)
labels = dataset.iloc[:,-1]
features = dataset.iloc[:, 0:-1]
print(features.columns)
features = pd.get_dummies(features)

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.33, random_state=25)

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.compose import ColumnTransformer

numerical_features = features.select_dtypes(include=['float64','int64'])
numerical_columns = numerical_features.columns
ct = ColumnTransformer([('only numeric',StandardScaler(),numerical_columns)], remainder='passthrough')

features_train_scaled = ct.fit_transform(features_train)
features_test_scaled = ct.transform(features_test)

from tensorflow.keras.models import Sequential
my_model = Sequential()

from tensorflow.keras.layers import InputLayer
input = InputLayer(input_shape = (features.shape[1],))

my_model.add(input)

from tensorflow.keras.layers import Dense
my_model.add(Dense(64, activation = 'relu'))
my_model.add(Dense(1))

print(my_model.summary())

from tensorflow.keras.optimizers import Adam
opt = Adam(learning_rate = 0.01)
my_model.compile(loss='mse',metrics=['mae'],optimizer=opt)

my_model.fit(features_train_scaled, labels_train, epochs=40,batch_size=1,verbose=1)

res_mse, res_mae = my_model.evaluate(features_test_scaled, labels_test, verbose=0)

print(f'Final loss (RMSE): {res_mse}')
print(f'Final Metric (MAE): {res_mae}')
