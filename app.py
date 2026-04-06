from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Apoorva Patel! Your DevOps project is LIVE 🚀 (VS CODE)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)