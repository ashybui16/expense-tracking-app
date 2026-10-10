# Sổ Chi Tiêu

Ứng dụng ghi chi tiêu bằng tiếng Việt, tính bằng VND. Gõ khoản chi như cách bạn nói. Chỉ một tệp, không cần thư viện, chỉ cần Python để chạy.

Bản trực tuyến (riêng tư, đồng bộ với tài khoản Claude): https://claude.ai/artifact/FUKoiCqQPhbhScFfxkVK7v

## Chạy trên máy

```sh
python3 build.py --serve   # rồi mở http://localhost:8000
```

Hoặc chạy `python3 build.py` rồi mở trực tiếp `index.html`. Khi chạy trên máy, dữ liệu được lưu trong localStorage của trình duyệt.

## Các tệp

- `src/tally.html`: toàn bộ ứng dụng (giao diện, kiểu dáng, mã). Viết dưới dạng một đoạn trang để đăng thẳng lên claude.ai.
- `build.py`: bọc đoạn trang thành tài liệu HTML đầy đủ và ghi ra `index.html`.
- `index.html`: tệp được tạo ra. Hãy sửa `src/tally.html` rồi build lại.

## Cách gõ nhanh

| Bạn gõ | Ứng dụng hiểu là |
|---|---|
| `cà phê sữa đá 29k` | 29.000 ₫ · Ăn uống · hôm nay |
| `grab 45k hôm qua` | 45.000 ₫ · Đi lại · hôm qua |
| `tiền nhà 6tr5 hàng tháng` | 6.500.000 ₫ · Nhà & hóa đơn · lặp lại hàng tháng |
| `tiền điện 1,2 triệu 3 ngày trước` | 1.200.000 ₫ · Nhà & hóa đơn |
| `quà sinh nhật mẹ 500k t7 tuần trước` | 500.000 ₫ · Mua sắm · thứ bảy tuần trước |
| `đi chợ 320.000đ ngày 28/9` | 320.000 ₫ · Đi chợ · 28/9 |
| `ca phe 30` | 30.000 ₫ (số dưới 1.000 được hiểu là nghìn đồng) |

Gõ có dấu hay không dấu đều được. Thêm `#ăn`, `#chợ`, `#mua`… để chọn danh mục. Ứng dụng nhớ bạn đã xếp một khoản vào danh mục nào.

## Tính năng

- **Tiền còn lại:** nhập số tiền bạn có trong tháng (gõ `15tr`, `15.000.000`…) để xem còn lại bao nhiêu sau khi chi, mỗi ngày còn tiêu được bao nhiêu và sau khi trừ hóa đơn định kỳ sắp tới còn bao nhiêu. Tháng chưa nhập sẽ dùng số của tháng gần nhất trước đó.
- **Tổng quan tháng:** đã chi bao nhiêu, so với tháng trước cùng thời điểm, dự kiến cả tháng (có tính các hóa đơn sắp tới) và số tiền mỗi ngày được tiêu.
- **Hũ chi tiêu:** ngân sách theo từng danh mục, có vạch đánh dấu mức nên chi đến hôm nay. Trong phần cài đặt có thể thêm danh mục mới, đổi tên (VD: “Ăn uống” thành “Ăn ngoài”) hoặc xóa danh mục; khoản chi của danh mục bị xóa chuyển sang “Khác”. Cũng có thể xóa “Khác”: khi đó nó chỉ hiện ở hũ chi tiêu nếu có khoản chi nằm trong đó, và khoản nào ứng dụng không tự xếp được thì bạn chọn danh mục. `#` cũng nhận tên mới.
- **Lịch chi tiêu:** bản đồ nhiệt theo ngày, đếm ngày không tiêu và chuỗi ngày không tiêu.
- **Khoản chi định kỳ:** tự tìm các khoản lặp lại hàng tháng và tính tổng mỗi năm.
- **Biên lai cuối tháng:** nhấn `r` để in tháng của bạn ra như một tờ hóa đơn, kèm “tiền thối lại” so với ngân sách.
- Xuất/nhập CSV, đổi tiền tệ, giao diện sáng/tối, phím tắt (`/` thêm, `[` `]` đổi tháng, `r` biên lai, `Esc` hủy).

Khi chưa có khoản chi nào, ứng dụng hiển thị một sổ mẫu (có ghi rõ là dữ liệu mẫu) để mọi phần đều có nội dung.
