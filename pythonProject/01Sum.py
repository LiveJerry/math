import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 读取数据
data = pd.read_excel(r'E:\math\SUM.xlsx')

# 复制数据以避免直接操作原始数据
features = data.copy()

# 使用 label_encoder 对分类名称进行编码
label_encoder = LabelEncoder()
features.loc[:, '分类名称'] = label_encoder.fit_transform(features['分类名称'])

# 合并相同单品名称的数据
merged_by_item = features.groupby('单品名称')['销售额'].sum().reset_index()

# 合并相同分类名称的数据
merged_by_category = features.groupby('分类名称')['销售额'].sum().reset_index()

# 将结果保存到新的 Excel 文件
with pd.ExcelWriter('sum02.xlsx') as writer:
    merged_by_item.to_excel(writer, sheet_name='按单品名称合并', index=False)
    merged_by_category.to_excel(writer, sheet_name='按分类名称合并', index=False)
