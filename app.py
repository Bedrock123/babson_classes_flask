from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def classes():
    d = {'hi': 'hi'}
    print 'hi'
    return jsonify(d)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)