from flask import Flask, render_template, request, jsonify
import os
import re

app = Flask(__name__)
LEAKS_DIR = 'data'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword', '').strip()
    if not keyword:
        return jsonify({'results': [], 'error': 'No keyword entered.'})

    results = []
    for file_name in os.listdir(LEAKS_DIR):
        if file_name.endswith('.txt'):
            file_path = os.path.join(LEAKS_DIR, file_name)
            try:
                with open(file_path, 'r', encoding='latin-1') as f:
                    for line in f:
                        if re.search(keyword, line, re.IGNORECASE):
                            results.append(line.strip())
            except Exception as e:
                continue

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
