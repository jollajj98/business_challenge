import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle
df = pd.read_csv("training_data.csv", index_col=0)
y = df["risk_level"]
x = df.drop(["risk_level"], axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)
regressor = LinearRegression()
regressor.fit(x_train, y_train)
print(regressor.coef_)
print(regressor.intercept_)
y_pred = regressor.predict(x_test)
print(regressor.score(x_test, y_test))
mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(mae, mse, rmse)
pickle_file = open("model.pkl", mode="wb")
pickle.dump(regressor, pickle_file)
pickle_file.close()