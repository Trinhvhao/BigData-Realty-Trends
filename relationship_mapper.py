#!/usr/bin/python3
"""mapper.py"""
import sys

# Đọc dữ liệu từ stdin
for line in sys.stdin:
    # Loại bỏ dấu cách và tách dòng dữ liệu theo dấu phẩy
    fields = line.strip().split(',')

    # Kiểm tra xem có đủ 12 trường hay không
    if len(fields) == 12:
        try:
            # Lấy giá trị diện tích và giá bán từ các cột trong dòng dữ liệu
            carpet_area = float(fields[9])  # Diện tích (cột thứ 10)
            sale_price = float(fields[4])  # Giá bán (cột thứ 5)

            # Kiểm tra xem diện tích và giá bán có hợp lệ (lớn hơn 0)
            if carpet_area > 0 and sale_price > 0:
                # Xuất diện tích và giá bán dưới dạng key-value
                # Key: diện tích, Value: giá bán
                print(f"{carpet_area}\t{sale_price}")
            else:
                # Nếu diện tích hoặc giá bán không hợp lệ, in ra thông báo (debug)
                print(f"Invalid data (area: {carpet_area}, price: {sale_price})", file=sys.stderr)

        except ValueError as e:
            # Nếu có lỗi chuyển đổi dữ liệu, bỏ qua dòng này và in lỗi ra stderr
            print(f"ValueError: {e} in line: {line}", file=sys.stderr)
    else:
        # Nếu không có đủ 11 trường, in thông báo (debug)
        print(f"Invalid number of fields: {len(fields)} in line: {line}", file=sys.stderr)
