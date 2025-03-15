#!/usr/bin/python3
"""mapper.py"""

import sys

# Đọc từng dòng dữ liệu từ input
for line in sys.stdin:
    # Tách các trường dữ liệu trên dấu phẩy (CSV)
    fields = line.strip().split(',')

    # Kiểm tra nếu số trường có ít nhất 11 trường và đảm bảo giá bán hợp lệ
    if len(fields) > 10:
        city = fields[2]  # Thành phố là cột thứ 3
        try:
            sale_price = float(fields[4])  # Giá bán là cột thứ 5
            # In ra (city, sale_price)
            print(f"{city}\t{sale_price}")
        except ValueError:
            pass  # Nếu giá bán không hợp lệ thì bỏ qua dòng đó
