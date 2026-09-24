# -*- coding: utf-8 -*-
"""Khung bài tập cho sinh viên: tự cài MỘT bước HITS (thuật toán MMDS §5.5.2, đề 5.5.1).

Đây là khung thực sự: sinh viên viết thuật toán trong hits_step bên dưới.
Không import mã hàm đáp án; kiểm tra bằng check_practice.py --student.
"""


def hits_step(adj, hub):
    """Một cặp cập nhật HITS với chuẩn hóa max.

    Input:
      adj : dict tên nút (str) -> danh sách đích (list[str]); mọi đích được kê; không có cạnh trùng.
      hub : dict tên nút -> điểm hub hiện tại (số không âm), cùng khóa với adj.

    Output:
      tuple (authority_new, hub_new): hai dict MỚI trên cùng khóa adj.

    Thuật toán (MMDS §5.5.2; chuẩn max theo sách):
      1. authority mới của đích v = TỔNG hub CŨ của mọi nguồn u có cạnh u->v.
         Gợi ý: TODO 1 — quét danh sách kề, cộng hub[u] vào a_new[v].
      2. Chuẩn hóa authority bằng cách chia cho phần tử lớn nhất.
         Nếu max = 0 (không có đóng góp nào), trả hai dict 0, KHÔNG chia 0.
      3. hub mới của nguồn u = TỔNG authority MỚI (sau chuẩn hóa) của các đích.
         Gợi ý: TODO 2 — cộng theo cạnh rồi chuẩn hóa max tương tự.

    Lưu ý: không teleport, không sửa adj/hub đầu vào, không cập nhật tại chỗ.
    """
    # TODO 1: tính authority thô theo cạnh nguồn -> đích từ hub cũ.
    # TODO 2: chuẩn hóa max, rồi tính hub mới từ authority MỚI và chuẩn hóa.
    raise NotImplementedError(
        "Sinh viên cài hits_step: cộng theo cạnh, chuẩn hóa max, hai dict mới.")
