import sys

# Mỗi từ phân cách bởi khoảng trắng đóng góp một lần xuất hiện.
for line in sys.stdin:
    for word in line.split():
        print(f"{word}\t1")
