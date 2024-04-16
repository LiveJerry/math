import pandas as pd

# 读取单品编码与分类名称的映射关系
category_mapping = pd.read_excel('01.xlsx')[['单品编码', '分类名称']]

# 读取每日销售数据，指定日期列名为 '销售日期'
sales_data = pd.read_excel('02.xlsx', parse_dates=['销售日期'])

# 读取批发价格数据
wholesale_prices = pd.read_excel('03.xlsx')

# 读取损耗率数据
loss_rates = pd.read_excel('04.xlsx')

# 合并销售数据、批发价格数据和损耗率数据
merged_data = pd.merge(sales_data, category_mapping, on='单品编码', how='left')
merged_data = pd.merge(merged_data, wholesale_prices, on=['日期', '单品编码'], how='left')
merged_data = pd.merge(merged_data, loss_rates, on='单品编码', how='left')

# 计算每个品类的销售额和成本
merged_data['销售成本'] = merged_data['销售单价(元/千克)'] * merged_data['销量(千克)'] * (1 + merged_data['损耗率(%)'] / 100)
category_sales = merged_data.groupby(['销售日期', '分类名称'])['销售单价(元/千克)', '销量(千克)', '销售成本'].sum().reset_index()

# 保存数据到SumTime01.xlsx
category_sales.to_excel('SumTime01.xlsx', index=False)
