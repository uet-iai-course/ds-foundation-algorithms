import sys
from itertools import groupby

# Hadoop đưa các dòng cùng khóa liền nhau; đọc nhóm lần lượt.
pairs = (line.rstrip("\n").split("\t", 1) for line in sys.stdin)
for word, group in groupby(pairs, key=lambda pair: pair[0]):
    total = sum(int(value) for _, value in group)
    print(f"{word}\t{total}")
