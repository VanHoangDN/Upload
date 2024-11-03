from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
app.config['MUSIC_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    # Danh sách các đuôi file hợp lệ
    allowed_extensions = ('.mp3', '.MP3', '.wma')
    
    # Lấy danh sách các file nhạc có đuôi hợp lệ trong thư mục
    music_files = [f for f in os.listdir(app.config['MUSIC_FOLDER']) if f.endswith(allowed_extensions)]
    return render_template('index.html', music_files=music_files)

@app.route('/music/<filename>')
def music(filename):
    return send_from_directory(app.config['MUSIC_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1886, debug=True)
