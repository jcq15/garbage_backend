from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    return '你是学术垃圾！'

if __name__ == '__main__':
    app.run(debug=True, port=8800)