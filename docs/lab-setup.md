# Lab Setup

## Cấu hình máy
- RAM 15.7 GB, WSL2 giới hạn 6 GB RAM / 4 CPU / 2 GB swap (`%USERPROFILE%\.wslconfig`)
- Docker Desktop (WSL2), Burp Suite Community v2026.8 chạy trên Windows host

## Target hiện tại
1. **OWASP Juice Shop** (`v20.2.0`, revision `5658473`), ghim phiên bản qua [`lab/juice-shop/.env`](../lab/juice-shop/.env) — cổng `127.0.0.1:3000`.
2. **Command Injection Lab** (Python 3.9 Flask + `iputils-ping`), đóng gói cục bộ qua [`lab/cmd-injection-lab/Dockerfile`](../lab/cmd-injection-lab/Dockerfile) — cổng `127.0.0.1:5000`.

## Vận hành

### 1. OWASP Juice Shop
```powershell
cd lab\juice-shop
Copy-Item .env.example .env      # lần đầu
docker compose up -d
docker compose logs --tail 5     # chờ "Server listening on port 3000"
curl.exe -I http://127.0.0.1:3000
docker compose down              # dừng và xóa container + mạng
```

### 2. Command Injection Lab
```powershell
cd lab\cmd-injection-lab
docker compose up -d --build     # build image và chạy nền
curl.exe -I http://127.0.0.1:5000
docker compose down              # dừng và xóa container + mạng
```

## Cô lập
- **Port Binding:** Chỉ publish ra loopback máy host (`127.0.0.1:3000` và `127.0.0.1:5000`); Burp listener chỉ lắng nghe tại `127.0.0.1:8080`.
- **Network:** Mỗi lab chạy trên một mạng bridge riêng biệt (`juice-shop_vulnlab_net` và `cmd-injection-lab_vulnlab_net`).
- **Hardening & Tài nguyên:**
  - `juice-shop`: `restart: "no"`, `cap_drop: ALL`, `no-new-privileges:true`, giới hạn `1g` RAM / `1.0` CPU.
  - `cmd-injection-lab`: `restart: "no"`, `no-new-privileges:true`, giới hạn `256m` RAM / `0.5` CPU (giữ capabilities mặc định để hỗ trợ `CAP_NET_RAW` cho lệnh `ping`).
- **Nguyên tắc an toàn chung:** Không dùng `--privileged`, `--network host`, hoặc mount `docker.sock`.

## Giới hạn đã biết
- Container hiện vẫn có đường ra Internet (chấp nhận được trong giai đoạn cài đặt gói và chạy target cơ bản; với các CVE nguy hiểm hơn có thể thêm `internal: true` vào cấu hình network).
- Tag `latest` và `v20.2.0` của Juice Shop cùng commit nguồn nhưng khác digest.
