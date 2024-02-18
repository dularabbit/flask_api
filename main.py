from flask import Flask, render_index

app = Flask(__name__)

@app.route('/')
def index():
    return render_index('index.html')

if __name__ == '__main__':
    app.run(debug=True, port="8000")
