"""气温与冷饮销量分析：请依次完成所有 TODO。"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / "data" / "daily_sales.csv"
FIGURE_PATH = PROJECT_DIR / "figures" / "scatter_fit.pdf"

# 1. 读取数据
data = pd.read_csv(DATA_PATH)
print("前五行数据：")
print(data.head())

# 2. 取出自变量 x 和因变量 y
x = data["temperature"].to_numpy()
y = data["sales"].to_numpy()

# TODO 1：输出数据的行数、列数和每列缺失值数量。

# TODO 2：计算 temperature 和 sales 的均值、标准差、最小值、最大值。
# 提示：可以使用 data[["temperature", "sales"]].describe()

# TODO 3：计算 Pearson 相关系数 r。
# 提示：np.corrcoef(x, y)[0, 1]

# TODO 4：拟合 y = slope * x + intercept。
# 提示：slope, intercept = np.polyfit(x, y, 1)

# TODO 5：利用 slope 和 intercept 计算每个样本的预测值 y_pred。

# TODO 6：计算残差、R² 和 RMSE，并打印全部结果。
# 提示：
# residuals = y - y_pred
# sse = np.sum((y - y_pred) ** 2)
# sst = np.sum((y - np.mean(y)) ** 2)
# r_squared = 1 - sse / sst
# rmse = np.sqrt(np.mean((y - y_pred) ** 2))

# TODO 7：绘制散点图和拟合直线。
# 建议先用 np.argsort(x) 得到排序索引，避免折线来回连接。
# plt.scatter(..., label="Observed data")
# plt.plot(..., label="Fitted line")
# 设置横纵轴标题、图例和浅色网格。

# TODO 8：取消下面两行的注释，保存并显示图片。
# FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)
# plt.savefig(FIGURE_PATH, bbox_inches="tight")
# plt.show()

