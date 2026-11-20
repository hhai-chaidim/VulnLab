# Sử dụng môi trường Python nhẹ nhất
FROM python:3.9-slim
WORKDIR /app
# Cài đặt thư viện Web Flask
RUN apt-get update && apt-get install -y --no-install-recommends iputils-ping \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir flask
# Copy file mã nguồn vào container
COPY app.py .
EXPOSE 5000
# Chạy ứng dụng
CMD ["python", "app.py"]