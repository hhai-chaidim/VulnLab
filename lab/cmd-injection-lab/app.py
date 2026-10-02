from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def ping():
    if request.method == 'POST':
        ip = request.form.get('ip', '')
        # Điểm chết (Injection Point): Biến 'ip' không được kiểm tra (sanitize)
        # mà truyền thẳng vào lệnh shell của hệ điều hành.
        command = f"ping -c 2 {ip}"
        
        try:
            # Thực thi lệnh và đọc kết quả trả về
            result = os.popen(command).read()
            return f"<h3>Kết quả Ping:</h3><pre>{result}</pre><a href='/'>Quay lại</a>"
        except Exception as e:
            return str(e)

    return '''
        <h2>Công cụ Kiểm tra Mạng</h2>
        <form method="post">
            Nhập IP để ping: <input type="text" name="ip" placeholder="127.0.0.1">
            <input type="submit" value="Ping">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)