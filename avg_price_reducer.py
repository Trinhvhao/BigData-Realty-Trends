#!/usr/bin/python3
"""reducer.py"""
import sys


current_city = None
total_price = 0
count = 0

# Đọc từng dòng từ input
for line in sys.stdin:
    line = line.strip()
    city, sale_price = line.split('\t')

    try:
        sale_price = float(sale_price)
    except ValueError:
        continue  # Bỏ qua dòng nếu không thể chuyển giá bán thành số

    # Kiểm tra nếu thành phố đã thay đổi
    if current_city == city:
        total_price += sale_price
        count += 1
    else:
        # Nếu có thành phố mới, in kết quả cũ và bắt đầu tính cho thành phố mới
        if current_city:
            avg_price = total_price / count if count > 0 else 0
            print(f"{current_city}\t{avg_price:.2f}")

        # Cập nhật thành phố và bắt đầu tính lại cho thành phố mới
        current_city = city
        total_price = sale_price
        count = 1

# In kết quả cuối cùng cho thành phố cuối cùng
if current_city == city:
    avg_price = total_price / count if count > 0 else 0
    print(f"{current_city}\t{avg_price:.2f}")
