"""气温与冷饮销量分析：描述统计、相关分析、一元线性回归与绘图。"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scienceplots


PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / "data" / "daily_sales.csv"
FIGURE_PATH = PROJECT_DIR / "figures" / "scatter_fit.pdf"

# 1. 读取数据，并确认建模所需字段存在
data = pd.read_csv(DATA_PATH)
required_columns = {"temperature", "sales"}
missing_columns = required_columns - set(data.columns)
if missing_columns:
    raise ValueError(f"数据缺少必要字段：{sorted(missing_columns)}")

print("前五行数据：")
print(data.head())

# 2. 取出自变量 x（日最高气温）和因变量 y（冷饮销量）
x = data["temperature"].to_numpy()
y = data["sales"].to_numpy()

# 3. 检查数据规模、缺失值和变量取值范围
row_count, column_count = data.shape
missing_count = data.isna().sum()

print("\n数据规模：")
print(f"行数：{row_count}")
print(f"列数：{column_count}")
print("每列缺失值数量：")
print(missing_count)

print("\n取值范围：")
print(f"气温：{x.min():.0f} 至 {x.max():.0f} °C")
print(f"销量：{y.min():.0f} 至 {y.max():.0f} 杯")

# 4. 计算气温和销量的均值、样本标准差、最小值与最大值
descriptive_stats = (
    data[["temperature", "sales"]]
    .describe()
    .loc[["mean", "std", "min", "max"]]
)

print("\n描述性统计：")
print(descriptive_stats.round(3))

# 5. 计算 Pearson 相关系数，衡量两个变量的线性相关程度
correlation = np.corrcoef(x, y)[0, 1]
print(f"\nPearson 相关系数 r：{correlation:.6f}")

# 6. 使用最小二乘法拟合 y = slope * x + intercept
slope, intercept = np.polyfit(x, y, 1)
print(f"回归斜率：{slope:.6f}")
print(f"回归截距：{intercept:.6f}")
print(f"拟合方程：y_hat = {intercept:.6f} + {slope:.6f} * x")

# 7. 计算样本预测值和残差
y_pred = slope * x + intercept
residuals = y - y_pred

# 8. 计算决定系数 R² 和均方根误差 RMSE
sse = np.sum(residuals**2)
sst = np.sum((y - np.mean(y)) ** 2)
r_squared = 1 - sse / sst
rmse = np.sqrt(np.mean(residuals**2))

print(f"决定系数 R²：{r_squared:.6f}")
print(f"均方根误差 RMSE：{rmse:.6f} 杯")

# 9. 使用 SciencePlots 绘制原始散点和拟合直线
# no-latex 让绘图不依赖本机 LaTeX；横坐标排序可避免折线来回连接。
plt.style.use(["science", "no-latex"])
sorted_index = np.argsort(x)

fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(
    x,
    y,
    color="#2878B5",
    s=35,
    label="Observed data",
    zorder=3,
)
ax.plot(
    x[sorted_index],
    y_pred[sorted_index],
    color="#C82423",
    linewidth=1.8,
    label="Fitted line",
)
ax.set_xlabel(r"Temperature ($^\circ$C)")
ax.set_ylabel("Sales (cups)")
ax.legend()
ax.grid(alpha=0.25)

# 10. 创建图片目录，将矢量图保存为 PDF，然后显示图形
FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(FIGURE_PATH, bbox_inches="tight")
print(f"\n拟合结果图已保存至：{FIGURE_PATH}")
plt.show()
