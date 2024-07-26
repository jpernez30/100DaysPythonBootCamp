from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from PIL import Image
from collections import Counter
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def get_most_common_colors(image_path, num_colors=5):
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = np.array(image.getdata())
    colors = Counter(map(tuple, pixels))
    most_common_colors = colors.most_common(num_colors)
    color_data = []
    for color, count in most_common_colors:
        # Calculate brightness
        brightness = sum(color)
        text_color = 'white' if brightness < 400 else 'black'
        color_data.append((color, count, text_color))
    return color_data

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            most_common_colors = get_most_common_colors(file_path)
            return render_template('results.html', colors=most_common_colors)
    return render_template('upload.html')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
