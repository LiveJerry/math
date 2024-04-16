import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# 设置全局字体
plt.rcParams['font.family'] = 'Arial Unicode MS'  # 使用支持中文字符的字体，如Arial Unicode MS

# 绘制图形的代码...

# 读取数据
data = pd.read_excel(r'E:\math\SUM.xlsx')

# 绘制分类名称销售额随季节变化的趋势图，并将图例放置在右侧
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='季节', y='销售额', hue='分类名称', marker='o')
plt.title('分类名称销售额随季节变化趋势')
plt.xlabel('季节')
plt.ylabel('销售额')
plt.grid(True)
plt.legend(title='分类名称', loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

# 绘制不同单品名称的销售额随季节变化的趋势图，并将图例放置在右侧
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='季节', y='销售额', hue='单品名称', marker='o')
plt.title('不同单品名称销售额随季节变化趋势')
plt.xlabel('季节')
plt.ylabel('销售额')
plt.grid(True)
plt.legend(title='单品名称', loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
