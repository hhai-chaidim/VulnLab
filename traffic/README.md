# Traffic — HTTP Captures

Thư mục này chứa các bản ghi HTTP request/response đã được **sanitize** (loại bỏ session cookie, token, thông tin nhạy cảm) từ Burp Suite.

## Cấu trúc

```
traffic/
└── CVE-YYYY-NNNNN/
    ├── 01-recon.md          # Request/response giai đoạn khảo sát
    ├── 02-exploit.md        # Request/response giai đoạn khai thác
    └── 03-remediation.md    # Request/response sau khi vá
```

## Quy tắc

- **KHÔNG** commit file `.burp`, `.har`, `.pcap` — chúng có thể chứa secret.
- Chỉ commit bản Markdown đã sanitize.
- Mỗi entry ghi rõ: method, URL, headers quan trọng, body, response status, response body.
- Ghi chú observation và conclusion riêng biệt.
