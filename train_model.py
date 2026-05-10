import pandas as pd
from sklearn.linear_model import LinearRegression

# 读取数据
data = pd.read_csv("training_data.csv")
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# 训练模型
model = LinearRegression()
model.fit(X, y)

# 保存模型参数到文件
with open("linear_model.txt", "w") as f:
    f.write("Linear Regression Model Coefficients:\n")
    f.write(f"Coefficients: {model.coef_}\n")
    f.write(f"Intercept: {model.intercept_}\n")

print("✅ Model trained and saved to linear_model.txt")