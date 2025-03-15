#!/usr/bin/python3
"""mapper.py"""
import sys
import csv

def read_input(file):
    for line in file:
        yield line.strip().split(",")

def main():
    input_stream = sys.stdin
    reader = csv.reader(input_stream)

    # Bỏ qua dòng tiêu đề
    header = next(reader, None)

    # Lấy index của cột "Property"
    property_index = header.index("Property") if header else -1

    if property_index == -1:
        sys.exit("Cột 'Property' không tồn tại!")

    for row in reader:
        if len(row) > property_index and row[property_index].strip():  # Kiểm tra dữ liệu hợp lệ
            print(f"{row[property_index]}\t1")

if __name__ == "__main__":
    main()
