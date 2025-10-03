import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("C:\\Users\\91886\\Desktop\\Dataset\\ml_homeprices.csv")

# Handle null values (fill bedrooms with median)
data['bedrooms'] = data['bedrooms'].fillna(data['bedrooms'].median())

# Regression plot: area vs price
sns.regplot(x="area", y="price", data=data,
            scatter_kws={'color':'blue'}, line_kws={'color':'black'})
plt.title("Regression Line: Area vs Price")
plt.show()

# Regression plot: bedrooms vs price
sns.regplot(x="bedrooms", y="price", data=data,
            scatter_kws={'color':'green'}, line_kws={'color':'black'})
plt.title("Regression Line: Bedrooms vs Price")
plt.show()


# Regression plot: age vs price
sns.regplot(x="age", y="price", data=data,
            scatter_kws={'color':'red'}, line_kws={'color':'black'})
plt.title("Regression Line: Age vs Price")
plt.show()

# Features & target
X = data[['area', 'bedrooms', 'age']]
y = data['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
