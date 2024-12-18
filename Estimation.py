import pandas as pd
import numpy as np

# 载入数据函数
def load_data(filepath):
    return pd.read_csv(filepath)

# 主数据处理函数
def process_financial_data(data):
    # 计算税后营业利润（NOPAT）
    nopat_percentage = 0.07  # NOPAT占销售额的比例
    data['NOPAT (百万美元)'] = data['销售额 (百万美元)'] * nopat_percentage

    # 自由现金流预测
    data['自由现金流 (股权, 百万美元)'] = data['NOPAT (百万美元)'] * 0.5  # 假设自由现金流为NOPAT的50%

    # 折现自由现金流以估算股权价值
    cost_of_equity = 0.12  # 股本成本
    discount_factors = np.array([1 / (1 + cost_of_equity)**(year - 1999) for year in data['年份']])
    data['折现后的自由现金流 (百万美元)'] = data['自由现金流 (股权, 百万美元)'] * discount_factors

    # 计算股权的总价值
    total_equity_value = np.sum(data['折现后的自由现金流 (百万美元)'])

    return data, total_equity_value

# 主函数
def main():
    filepath = 'MaxwellShoe_FinancialForecast_Corrected.csv'
    financial_data = load_data(filepath)
    processed_data, total_equity_value = process_financial_data(financial_data)
    
    print("Processed Financial Data:")
    print(processed_data)
    print("Total Equity Value (百万美元):", total_equity_value)

if __name__ == "__main__":
    main()
