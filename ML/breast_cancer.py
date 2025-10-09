import matplotlib as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error,r2_score
# load data
cancer=datasets.load_breast_cancer()

# print(cancer.keys())
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
x=cancer.data
y=cancer.frame

X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.20, random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

# predication
y_pred=model.predict(X_test)


print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))