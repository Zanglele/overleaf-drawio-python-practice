# 基于一元线性回归的气温与冷饮销量关系分析

## 项目简介

本项目使用连续 15 天的日最高气温和校园冷饮店销量数据，完成数据检查、描述性统计、Pearson 相关分析和一元线性回归建模，并生成适用于 LaTeX 论文的矢量图。

项目的主要目标是完整实践以下流程：

```text
读取数据 → 数据检查 → 描述性统计 → 相关分析 → 线性回归
→ 模型评价 → 结果绘图 → LaTeX 写作 → Overleaf 编译
```

## 目录结构

```text
.
├── README.md
├── TASK_GUIDE.md
├── analysis.py
├── main.tex
├── data
│   └── daily_sales.csv
└── figures
    ├── README.md
    ├── scatter_fit.pdf
    ├── workflow.drawio
    └── workflow.pdf
```

主要文件说明：

- `analysis.py`：数据检查、统计分析、线性回归、模型评价和绘图代码。
- `main.tex`：已填写核心研究内容的中文论文源码。
- `data/daily_sales.csv`：包含日序号、日最高气温和冷饮销量的原始数据。
- `figures/scatter_fit.pdf`：散点图与线性拟合结果。
- `figures/workflow.pdf`：论文使用的分析流程图。
- `figures/workflow.drawio`：流程图的可编辑源文件。
- `TASK_GUIDE.md`：原始练习要求和验收清单。

## Python 环境

建议使用 Python 3.10 或更高版本，并安装以下依赖：

```powershell
python -m pip install numpy pandas matplotlib SciencePlots
```

使用 `python -m pip` 可以尽量确保依赖安装到当前正在运行代码的 Python 解释器中。

## 运行数据分析

在项目根目录中运行：

```powershell
python analysis.py
```

程序会依次输出：

1. 数据前五行；
2. 数据行数、列数和缺失值数量；
3. 气温与销量的取值范围；
4. 均值、样本标准差、最小值和最大值；
5. Pearson 相关系数；
6. 回归斜率、截距和拟合方程；
7. 决定系数和均方根误差；
8. 拟合图的保存位置。

运行完成后会生成或更新：

```text
figures/scatter_fit.pdf
```

## 核心结果

数据共有 15 条观测和 3 个字段，所有字段均无缺失值。主要计算结果为：

```text
Pearson 相关系数：r = 0.998479
回归截距：1.205952
回归斜率：4.346429
决定系数：R² = 0.996960
均方根误差：RMSE = 1.036975 杯
```

拟合方程为：

```text
ŷ = 1.205952 + 4.346429x
```

在当前样本范围内，气温每升高 1 摄氏度，模型预测冷饮销量平均增加约 4.35 杯。该结果反映的是统计相关关系，不能单独证明因果关系。

## 在 Overleaf 中编译

1. 将整个项目压缩为 ZIP 并上传到 Overleaf。
2. 确认主文件为 `main.tex`。
3. 在项目设置中将编译器设置为 **XeLaTeX**。
4. 在 `main.tex` 中填写姓名和学号。
5. 点击重新编译，生成论文 PDF。

`main.tex` 使用以下固定图片路径：

```text
figures/workflow.pdf
figures/scatter_fit.pdf
```

不要随意修改图片文件名，否则论文会显示图片占位框。

## 当前完成状态

- [x] 原始数据检查
- [x] 描述性统计
- [x] Pearson 相关分析
- [x] 一元线性回归
- [x] R² 和 RMSE 计算
- [x] 拟合结果图
- [x] 分析流程图
- [x] 论文核心内容
- [x] Overleaf XeLaTeX 最终编译

## 注意事项

- 原始数据完整，不需要为了展示“数据清洗”而删除或修改样本。
- 当前结论来自 15 天的小样本，模型的样本内拟合效果不等于未来预测精度。
- 销量还可能受到降雨、节假日、促销和客流量等因素影响。
- 如果提示找不到 `scienceplots`，请确认依赖安装到了实际运行 `analysis.py` 的 Python 解释器中。
- 提交前应检查图题、表题、公式编号、正文引用和页面空白。
