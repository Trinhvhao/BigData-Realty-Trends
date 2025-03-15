import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
df = pd.read_csv("V3_cleaned.csv")

# Đổi tên cột cho dễ làm việc
df.columns = ["Date", "Year", "Locality", "Estimated_Value", "Sale_Price", "Property",
              "Residential", "Num_Rooms", "Num_Bathrooms", "Carpet_Area", "Property_Tax_Rate", "Face"]

# Chuyển đổi kiểu dữ liệu
df["Sale_Price"] = pd.to_numeric(df["Sale_Price"], errors="coerce")
df["Carpet_Area"] = pd.to_numeric(df["Carpet_Area"], errors="coerce")

# Bỏ các hàng có giá trị thiếu
df_clean = df.dropna(subset=["Sale_Price", "Carpet_Area"])

# Xác định các outliers theo IQR (Interquartile Range)
Q1 = df_clean["Sale_Price"].quantile(0.25)
Q3 = df_clean["Sale_Price"].quantile(0.75)
IQR = Q3 - Q1

# Giới hạn dữ liệu trong khoảng hợp lý
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_clean = df_clean[(df_clean["Sale_Price"] >= lower_bound) & (df_clean["Sale_Price"] <= upper_bound)]

# Biểu đồ trước và sau khi làm sạch
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(df["Sale_Price"], bins=50, kde=True, ax=axes[0])
axes[0].set_title("Trước khi làm sạch")

sns.histplot(df_clean["Sale_Price"], bins=50, kde=True, ax=axes[1])
axes[1].set_title("Sau khi làm sạch")

plt.show()

# Lưu file đã làm sạch
df_clean.to_csv("Cleaned_Data.csv", index=False)

print("Hoàn thành làm sạch dữ liệu. File đã lưu thành 'Cleaned_Data.csv'.")
