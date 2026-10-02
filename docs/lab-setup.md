# Lab Setup

## Cấu hình máy
- RAM 15.7 GB, WSL2 giới hạn 6 GB RAM / 4 CPU / 2 GB swap (`%USERPROFILE%\.wslconfig`)
- Docker Desktop (WSL2), Burp Suite Community v2026.8 chạy trên Windows host

## Target hiện tại
- OWASP Juice Shop v20.2.0 (revision 5658473), ghim qua `lab/juice-shop/.env`

## Vận hành
```powershell
cd lab\juice-shop
Copy-Item .env.example .env      # lần đầu
docker compose up -d
docker compose logs --tail 5     # chờ "Server listening on port 3000"
curl.exe -I http://127.0.0.1:3000
docker compose down              # dừng và xóa container + mạng
```

## Cô lập
- Port chỉ publish `127.0.0.1:3000`; Burp listener `127.0.0.1:8080`
- `cap_drop: ALL`, `no-new-privileges`, giới hạn 1 GiB RAM / 1 CPU
- Không dùng `--privileged`, `--network host`, `docker.sock`

## Giới hạn đã biết
- Container vẫn có đường ra Internet (chấp nhận với Juice Shop; cần chặn riêng cho target nguy hiểm hơn).
- Tag `latest` và `v20.2.0` cùng commit nguồn nhưng khác digest.
- `lab/cmd-injection-lab` chưa được chạy; cần cô lập thêm trước khi dùng.
