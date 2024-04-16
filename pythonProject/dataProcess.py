import pandas as pd

# 读取销售数据
sales_data = pd.read_excel(r'E:\math\02.xlsx')

# 将销售日期转换为日期时间格式
sales_data['销售日期'] = pd.to_datetime(sales_data['销售日期'], format='%Y/%m/%d')

# 将日期转换为季节
def get_season(month):
    if month in [3, 4, 5]:
        return '春季'
    elif month in [6, 7, 8]:
        return '夏季'
    elif month in [9, 10, 11]:
        return '秋季'
    else:
        return '冬季'

sales_data['季节'] = sales_data['销售日期'].dt.month.map(get_season)

# 计算销售额
sales_data['销售额'] = sales_data['销量(千克)'] * sales_data['销售单价(元/千克)']

# 按季节和单品编码进行分组，并计算总销售额
seasonal_sales = sales_data.groupby(['季节', '单品编码'])['销售额'].sum().reset_index()

# 读取附件一中的数据
attachment_data = pd.read_excel(r'E:\math\01.xlsx')

# 合并单品信息
merged_data = pd.merge(seasonal_sales, attachment_data, left_on='单品编码', right_on='单品编码', how='left')

# 保存结果到 Excel 文件
merged_data.to_excel(r'E:\math\SUM.xlsx', index=False)

print("按季节统计的销售额已保存到 SUM.xlsx 文件中。")
