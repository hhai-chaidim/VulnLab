# Test Results — VulnLab

Tài liệu này ghi nhận kết quả thực tế khi thực thi các kịch bản kiểm thử trong [`test-plan.md`](./test-plan.md).

---

## 1. Lab Validation

| ID | Mô tả | Kết quả | Bằng chứng & Ghi chú thực tế |
|----|-------|---------|------------------------------|
| **LAB-01** | Juice Shop khởi động thành công | **PASS** | Container `vulnlab_juiceshop` (`v20.2.0`) trạng thái `Up`; `Invoke-WebRequest http://127.0.0.1:3000` trả về `StatusCode 200`. |
| **LAB-02** | Juice Shop chỉ bind `127.0.0.1` | **PASS** | Kiểm tra `netstat -ano \| Select-String ":3000"` xác nhận chỉ lắng nghe trên `127.0.0.1:3000`, không mở trên `0.0.0.0` hay LAN IP. |
| **LAB-03** | `cmd-injection-lab` khởi động | **PASS** | Sau khi bổ sung `iputils-ping` vào `Dockerfile`, `GET http://127.0.0.1:5000` trả về đúng form HTML và `POST ip=127.0.0.1` ping thành công (`0% packet loss`). |
| **LAB-04** | `cmd-injection-lab` chỉ bind `127.0.0.1` | **PASS** | Kiểm tra `netstat -ano \| Select-String ":5000"` xác nhận chỉ lắng nghe trên `127.0.0.1:5000`. |
| **LAB-05** | Burp Suite proxy intercept hoạt động | **PASS** | Đã bắt được HTTP traffic qua Burp Listener `127.0.0.1:8080`. Bằng chứng lưu tại [`evidence/lab-setup/burp-http-history.png`](../evidence/lab-setup/burp-http-history.png) (SHA-256 trong `hashes.txt`). |
| **LAB-06** | Dừng lab sạch sẽ | **PASS** | Lệnh `docker compose down` trên cả 2 lab đã gỡ bỏ hoàn toàn container (`Removed`) và mạng bridge riêng (`Removed`). |

---

## 2. Vulnerability Validation

> **Trạng thái:** `PENDING` — Sẽ cập nhật khi tiến hành giai đoạn phân tích CVE và đối chiếu bản vá (Remediation).

---

## 3. Code Validation (CVE Lab Notebook)

> **Trạng thái:** `PENDING` — Sẽ cập nhật khi xây dựng bộ Unit Tests cho công cụ Python CLI trong Phase 4.
