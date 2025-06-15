from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Tekton CI Flask App!"

@app.route('/info')
def info():
    return jsonify({
        "db_url": os.getenv('DB_URL', 'Not set'),
        "jwt_secret": os.getenv('JWT_SECRET', 'Not set')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)