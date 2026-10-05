# Test Plan — VulnLab

## Mục đích

Tài liệu này mô tả các bài kiểm tra cần thực hiện cho từng giai đoạn của project.

---

## Lab Validation Tests

| ID | Mô tả | Điều kiện Pass |
|----|-------|----------------|
| LAB-01 | Juice Shop khởi động thành công | `curl http://127.0.0.1:3000` trả về HTTP 200 |
| LAB-02 | Juice Shop chỉ bind 127.0.0.1 | `curl http://<LAN_IP>:3000` thất bại |
| LAB-03 | cmd-injection-lab khởi động | `curl http://127.0.0.1:5000` trả về form HTML |
| LAB-04 | cmd-injection-lab chỉ bind 127.0.0.1 | `curl http://<LAN_IP>:5000` thất bại |
| LAB-05 | Burp Suite proxy intercept hoạt động | Thấy traffic trong HTTP History |
| LAB-06 | Dừng lab sạch sẽ | `docker compose down` không để lại container/network |

## Vulnerability Validation Tests

> Sẽ bổ sung khi bắt đầu research CVE cụ thể.

## Code Validation Tests (CVE Notebook)

> Sẽ bổ sung khi phát triển CLI tool (Phase 4).
