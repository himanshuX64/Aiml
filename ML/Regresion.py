import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error,r2_score

# load data
data=pd.read_csv("C:\\Users\\91886\\Desktop\\Aiml\\Dataset\\canada_per_capita_income.csv")


# independent varible and  dependent variable
X=data[['year']]  # independent variable must be 2d
Y=data['per capita income (US$)']

# Train test split

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.33, random_state=42)



# # standardizing data
# from sklearn.preprocessing import StandardScaler
# scaler=StandardScaler()
# X_train=scaler.fit_transform(X_train)
# X_test=scaler.transform(X_test) 
# print(X_train)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,y_train)

# prediction
y_pred=model.predict(X_test)

# Evaluate model
print("Slope is :",model.coef_[0])
print("Intercep is :",model.intercept_)
print("MSE is :",mean_squared_error(y_test,y_pred))
print("R^2 Score is :",r2_score(y_test,y_pred))

# Visual
plt.scatter(X_train,y_train,color='blue',label='training data')
plt.scatter(X_test,y_test,color='green',label='Test data')
plt.plot(X,model.predict(X),color='red',label='Regression Line')
plt.xlabel('year')
plt.ylabel('Per capita income')
plt.title('Simple Linear regression')
plt.legend()
plt.show()