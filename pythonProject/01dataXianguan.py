import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# 设置全局字体
plt.rcParams['font.family'] = 'Arial Unicode MS'  # 使用支持中文字符的字体，如Arial Unicode MS

# 绘制图形的代码...

# 读取数据
data = pd.read_excel(r'SUM02.xlsx')

# 选择单品名称和销售额作为特征
X = data[['单品名称', '销售额']]

# 层次聚类
Z = linkage(X.set_index('单品名称'), method='ward')

# 输出树状图并保存为1.png
plt.figure(figsize=(70, 30))  # 调整图像大小，增加宽度
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
dendrogram(
    Z,
    labels=X['单品名称'].values,  # 使用单品名称作为标签
    leaf_rotation=90.,
    leaf_font_size=8.,
)
plt.tight_layout()  # 调整布局以确保标签可见
plt.savefig('1.png', dpi=300)  # 保存为1.png，并设置分辨率为300dpi