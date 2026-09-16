# Thực hành đếm từ với Hadoop và Docker Compose

Thực hành bài **đếm từ (word count)** — cài đặt giảng dạy điển hình của MapReduce
(theo MMDS §2.2) dùng **Hadoop Streaming** với Python, chạy trên cụm Hadoop giả lập
bằng Docker Compose.

Bộ lab **đã được kiểm chứng runtime** trên Linux amd64 với Docker Compose v5.5.1
(`docker compose version`), Hadoop 3.4.2, Python 3.10.12. Chỉ ghi nhận môi trường
đã kiểm; chưa kiểm trên ARM và không cam kết kết quả giống hệt trên máy hoặc
nền tảng khác.

Image dùng sẵn (không Dockerfile, không build):
`apache/hadoop:3.4.2-lean@sha256:27eb85ba5765b79fd0cde5a245579a3c5ab93799016a44dd0c447a13e64cb790`
(platform `linux/amd64`, kèm Python 3.10.12).
Hadoop/Java được tải về từ Docker Hub, **không cần cài Java trên máy local**.

## Cấu trúc

```
hadoop-compose/
├── compose.yaml     # 6 services: namenode, datanode1/2, resourcemanager, nodemanager1/2
├── config           # env_file cấu hình Hadoop (core/hdfs/mapred/yarn/capacity-scheduler)
├── mapper.py        # mapper Python (stdin -> word\t1)
├── reducer.py       # reducer + combiner Python (itertools.groupby, bộ nhớ hằng số/key)
├── run-job.sh       # script nộp job Streaming, chạy trong namenode
├── data/
│   ├── d1.txt       # "mèo chó mèo"
│   └── d2.txt       # "chó chim"
└── README.md
```

## Sinh viên cần làm gì

1. Cài Docker và Compose trước lớp (mục Cài đặt Docker).
2. Tải và giải nén bộ mã, vào thư mục lab.
3. Khởi động cụm, chờ đủ 2 DataNode Live và 2 NodeManager RUNNING.
4. Nộp job, đối chiếu kết quả với đếm thủ công, xem bộ đếm từng pha.
5. Trả lời ba câu hỏi kiểm tra ở slide cuối; dọn dẹp theo mục Dọn dẹp.

## Cụm gồm 6 container

| Service          | Chức năng                     | Port host (chỉ 127.0.0.1) |
|------------------|-------------------------------|---------------------------|
| `namenode`       | HDFS NameNode                 | 19870 → 9870 (Web UI)     |
| `datanode1`      | HDFS DataNode                 | —                         |
| `datanode2`      | HDFS DataNode                 | —                         |
| `resourcemanager`| YARN ResourceManager          | 18088 → 8088 (Web UI)     |
| `nodemanager1`   | YARN NodeManager              | —                         |
| `nodemanager2`   | YARN NodeManager              | —                         |

Toàn bộ service dùng chung một image anchor (`x-hadoop-common`), cùng một bridge
mặc định, hostname trùng tên service. Không privileged, không mount Docker socket.

**Lưu ý dữ liệu:** không dùng volume HDFS. Dữ liệu HDFS **được giữ khi `stop`/`start`**
(nhưng mất khi container bị recreate). Lệnh `docker compose down` **xoá container và
toàn bộ dữ liệu HDFS** — **đọc kỹ phần Dọn dẹp ngay trước khi chạy lệnh**, backup kết quả
cần giữ (`hdfs dfs -cat ...` ra máy local) trước khi chạy `down`.

**Cấu hình nổi bật trong `config`:**
- `fs.defaultFS=hdfs://namenode:8020`, `dfs.replication=2` (đúng 2 DataNode).
- MapReduce trên YARN, `HADOOP_MAPRED_HOME=/opt/hadoop` (đường dẫn tuyệt đối, tránh
  `$` để Compose không interpolate).
- NodeManager: 2048 MB / 2 vcores; map/reduce/AM 512 MB, `-Xmx256m`;
  `maximum-am-resource-percent=0.5` để lab nhỏ đủ tài nguyên chạy ApplicationMaster;
  tắt kiểm tra pmem/vmem (mô phỏng trên máy cá nhân).
- Capacity scheduler default giữ nguyên từ nguồn chính thức.
- Log aggregation bật; **không có history server**, nên trang history của job hoàn tất
  không có. Log xem qua `yarn logs -applicationId <appId>` — aggregation ghi lên HDFS,
  có thể phải chờ aggregation hoàn tất trước khi log sẵn sàng.
- Daemon giới hạn `HADOOP_HEAPSIZE_MAX=512`; `mem_limit`: NN/RM 1g, DN 768m, NM 3g.

**Ngân sách đề nghị cho máy host (cấu hình lab đề nghị, không phải số đo thực nghiệm):
Docker ~10 GB RAM, 4 CPU, ~5 GB disk.** Đây là cấu hình đề nghị cho máy chạy cụm. Trên Docker Desktop ARM, image amd64 chạy qua
emulation nên có thể chậm (chưa kiểm).

## Cài đặt Docker

Cài Docker Engine kèm Compose plugin (Linux), hoặc Docker Desktop, theo hướng dẫn
chính thức: https://docs.docker.com/compose/install/

## Tải mã lab

Tải [bộ mã ZIP](../hadoop-compose.zip), giải nén, rồi:

```bash
cd hadoop-compose
```

Hoặc clone kho và vào thư mục `2627-1/examples/lec-02/hadoop-compose`.

## Khởi động

```bash
docker compose pull
docker compose up -d
```

Chờ cụm sẵn sàng — cần **2 DataNode "Live"** và **2 NodeManager "Running"**:

```bash
# HDFS: 2 DataNode live
docker compose exec namenode hdfs dfsadmin -report | grep 'Live datanodes' -A 5

# YARN: 2 NodeManager RUNNING
docker compose exec namenode yarn node -list
```

Kiểm tra Python trong container (đủ để xác nhận môi trường; không cần inspect tag —
khi pull theo digest, tag cục bộ có thể không nhất thiết tồn tại):

```bash
docker compose exec namenode python3 --version   # Python 3.10.12
```

## Chạy job đếm từ

`run-job.sh` chạy **trong container namenode** (script tự chờ thoát safe mode, in
`hdfs dfsadmin -report` và `yarn node -list` trước khi nộp job; mỗi lần chạy tạo thư
mục output duy nhất `/user/hadoop/lec02/run-<TIMESTAMP>-<PID>`, **không xoá output cũ**):

```bash
docker compose exec -T namenode bash /work/run-job.sh
```

Script nộp job Streaming với 2 reducer, dùng `mapper.py` / `reducer.py` (reducer cũng
được khai báo làm combiner — sum là phép kết hợp giao hoán nên hợp lệ; Hadoop có thể
hoặc không chạy combiner, kết quả cuối không đổi), rồi `hdfs dfs -cat` các `part-*`.

Kết quả mong đợi trên dữ liệu mẫu: `chó 2`, `chim 1`, `mèo 2`.

Lần chạy kiểm chứng thực tế: 2 Map, 2 Reduce; bộ đếm ghi 5 cặp Map output,
4 cặp sau Combine, 3 cặp Reduce output. Số cặp Combine có thể khác giữa các
lần nộp job. Log job lấy qua `yarn logs -applicationId <appId>` với
`applicationId` in ở output của job; có thể phải chờ aggregation hoàn tất.
Không có history server nên không dùng proxy history.

## Kiểm chứng & Quan sát

- **Web UI HDFS NameNode:** http://127.0.0.1:19870 (Datanodes tab → 2 node live).
- **Web UI YARN ResourceManager:** http://127.0.0.1:18088 (Applications/Nodes).
- **fsck — xem block và replica của input:**

  ```bash
  docker compose exec namenode hdfs fsck /user/hadoop/lec02 -files -blocks -locations
  ```

  Với replication=2, mỗi block có 2 bản sao trên 2 DataNode.

## Phân biệt khái niệm (đọc kỹ để tránh hiểu sai)

- **YARN container ≠ Docker container.** "Container" trong YARN/ResourceManager UI là
  đơn vị cấp phát tài nguyên của một task (map/reduce/AM). Cụm Docker này chỉ có
  **6 Docker container**; số YARN container thay đổi theo job.
- **1 máy host:** 2 DataNode/2 NodeManager chạy trên cùng một máy vật lý, **không mô
  phỏng lỗi host/rack độc lập**, và không chứng minh được speedup của phân tán thực.
- DataNode và NodeManager nằm ở **container tách biệt** — không thể tuyên bố
  "local reading" (data locality thật giữa process DN và NM trên cùng node).
- Hai bản sao HDFS nằm trong hai Docker container trên **cùng một ổ đĩa của máy
  chủ**; tổng dung lượng Hadoop báo không phải hai ổ độc lập.
- **Giới hạn đầu vào:** mapper giữ nguyên chữ hoa/thường và dấu câu (chỉ tách theo
  whitespace) — ngoài phạm vi bài này. Input rỗng/đếm lớn: dùng `int` của Python
  (độ chính xác tuỳ ý).
- **Ngưỡng tách 128 MiB** giữ mỗi tệp mẫu thành 1 split → 2 Map, để đối chiếu
  trực tiếp trên dữ liệu mẫu; không phải tối ưu cho dữ liệu lớn.
- **Hàm băm mặc định:** với 2 Reduce, một part có thể rỗng và 2 Reduce không bảo
  đảm cân bằng tải; tổng số từ vẫn là 5.

## Dọn dẹp

```bash
docker compose stop        # giữ container + dữ liệu HDFS
docker compose start       # dùng lại
# CẢNH BÁO: lệnh sau xoá container và toàn bộ dữ liệu HDFS —
# đọc lưu ý dữ liệu ở trên và backup kết quả cần giữ trước khi chạy.
docker compose down
```

## Nguồn tham khảo

- Image và hướng dẫn chính thức: https://hub.docker.com/r/apache/hadoop
- Compose mẫu chính thức của Apache Hadoop: https://github.com/apache/hadoop/blob/docker-hadoop-3.4.2/docker-compose.yaml
- Hadoop Streaming 3.4.2: https://hadoop.apache.org/docs/r3.4.2/hadoop-streaming/HadoopStreaming.html
- MMDS §2.2 (MapReduce, bài đếm từ): Leskovec, Rajaraman, Ullman — *Mining of Massive Datasets*.
