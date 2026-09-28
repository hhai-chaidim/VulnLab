# Sử dụng môi trường Python nhẹ nhất
FROM python:3.9-slim
WORKDIR /app
# Cài đặt thư viện Web Flask
RUN pip install flask
# Copy file mã nguồn vào container
COPY app.py .
EXPOSE 5000
# Chạy ứng dụng
CMD ["python", "app.py"]