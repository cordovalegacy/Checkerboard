from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', num_1 = 8, num_2 = 8)

@app.route('/<int:num_1>')
def row(num_1):
    return render_template('index.html', num_1 = num_1, num_2 = 8)

@app.route('/<int:num_1>/<int:num_2>')
def row_and_col(num_1, num_2):
    return render_template('index.html', num_1 = num_1, num_2 = num_2)

@app.route('/<int:num_1>/<int:num_2>/<color_1>')
def board_color_1(num_1, num_2, color_1):
    return render_template('index.html', num_1 = num_1, num_2 = num_2, color_1 = color_1)

@app.route('/<int:num_1>/<int:num_2>/<color_1>/<color_2>')
def board_color_2(num_1, num_2, color_1, color_2):
    return render_template('index.html', num_1 = num_1, num_2 = num_2, color_1 = color_1, color_2 = color_2)

if __name__=='__main__':
    app.run(debug=True)