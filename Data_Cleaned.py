import pandas as pd
from datetime import datetime

# Đọc file dữ liệu
file_path = "Data.csv"
df = pd.read_csv(file_path)

# Xử lý giá trị thiếu
df['Locality'].fillna('Unknown', inplace=True)
df['Estimated Value'].fillna(df['Estimated Value'].mean(), inplace=True)
df['carpet_area'].fillna(df['carpet_area'].mean(), inplace=True)

# Chuyển đổi định dạng ngày tháng
def convert_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        return None  # Đánh dấu lỗi nếu có

df['Date'] = df['Date'].astype(str).apply(convert_date)
df.dropna(subset=['Date'], inplace=True)  # Loại bỏ dòng có lỗi ngày tháng

# Chuẩn hóa dữ liệu dạng text
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Lưu file kết quả
output_path = "V3_cleaned.csv"
df.to_csv(output_path, index=False)

print(f"Dữ liệu đã xử lý và lưu vào {output_path}")
