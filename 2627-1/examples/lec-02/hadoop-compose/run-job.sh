#!/usr/bin/env bash
# Chạy bài đếm từ bằng Hadoop Streaming, thực thi TRONG container namenode:
#   docker compose exec -T namenode bash /work/run-job.sh
set -euo pipefail

# 1. Chờ HDFS thoát safe mode.
hdfs dfsadmin -safemode wait

# 2. Kiểm tra trạng thái cụm trước khi nộp job.
hdfs dfsadmin -report
yarn node -list

# 3. Tạo thư mục output DUY NHẤT mỗi lần chạy, không xoá output cũ.
RUN_DIR="/user/hadoop/lec02/run-$(date +%s)-$$"
INPUT_DIR="${RUN_DIR}/input"
OUTPUT_DIR="${RUN_DIR}/output"

hdfs dfs -mkdir -p "${INPUT_DIR}"
hdfs dfs -put /work/data/*.txt "${INPUT_DIR}"

# 4. Nộp job Streaming: 2 reducer, mapper/reducer/combiner bằng Python 3.
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar \
  -D mapreduce.job.reduces=2 \
  -D mapreduce.input.fileinputformat.split.minsize=134217728 \
  -files /work/mapper.py,/work/reducer.py \
  -input "${INPUT_DIR}" \
  -output "${OUTPUT_DIR}" \
  -mapper 'python3 mapper.py' \
  -combiner 'python3 reducer.py' \
  -reducer 'python3 reducer.py'

# 5. In kết quả.
echo "Output directory: ${OUTPUT_DIR}"
hdfs dfs -cat "${OUTPUT_DIR}/part-*"
