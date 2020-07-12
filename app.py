from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input')
def ask():
    return render_template('input.html')

@app.route('/output' , methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('output.html', result=result)

# if __name__ == '__main__':
#     app.run(debug=True)

# 아래 터미널에서 Ctrl+C로 끊고 flask run으로 재시작