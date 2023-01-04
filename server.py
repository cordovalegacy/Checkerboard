from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', num_1 = 8, num_2 = 8)

if __name__=='__main__':
    app.run(debug=True)