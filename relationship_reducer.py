#!/usr/bin/python3
"""reducer.py"""
import sys

# Khởi tạo các biến để tính toán tổng diện tích, tổng giá bán, tổng diện tích * giá bán
total_area = 0
total_price = 0
total_area_price = 0
count = 0

# Đọc dữ liệu từ stdin (được truyền từ mapper)
for line in sys.stdin:
    # Tách các trường dữ liệu bằng dấu tab
    area, price = line.strip().split('\t')

    try:
        # Chuyển diện tích và giá bán thành kiểu số
        area = float(area)
        price = float(price)

        # Cộng dồn diện tích, giá bán, diện tích * giá bán và số lượng
        total_area += area
        total_price += price
        total_area_price += area * price
        count += 1

        # In ra cặp diện tích và giá bán
        print(f"Area: {area}, Price: {price}")

    except ValueError:
        continue  # Nếu có lỗi chuyển đổi, bỏ qua dòng này

# Sau khi nhận hết dữ liệu từ mapper, tính toán hệ số tương quan
if count > 0:
    # Tính toán các hệ số cần thiết cho hệ số tương quan
    mean_area = total_area / count
    mean_price = total_price / count

    # Tính toán hệ số tương quan (Pearson correlation coefficient)
    numerator = total_area_price - (total_area * total_price / count)
    denominator = ((total_area**2 - total_area * mean_area) / count) ** 0.5 * ((total_price**2 - total_price * mean_price) / count) ** 0.5

    if denominator != 0:
        correlation = numerator / denominator
    else:
        correlation = 0  # Nếu mẫu dữ liệu không đủ, hệ số tương quan là 0

    # In ra kết quả hệ số tương quan
    print(f"Correlation coefficient between area and price: {correlation}")
else:
    print("No valid data to compute correlation.")
