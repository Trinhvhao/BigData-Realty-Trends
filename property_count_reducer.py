#!/usr/bin/python3
"""reducer.py"""
#!/usr/bin/env python3
import sys

def main():
    current_property = None
    current_count = 0

    for line in sys.stdin:
        property_type, count = line.strip().split("\t")

        try:
            count = int(count)
        except ValueError:
            continue  # Bỏ qua nếu giá trị không hợp lệ

        if current_property == property_type:
            current_count += count
        else:
            if current_property:
                print(f"{current_property}\t{current_count}")
            current_property = property_type
            current_count = count

    # In kết quả cuối cùng
    if current_property:
        print(f"{current_property}\t{current_count}")

if __name__ == "__main__":
    main()
