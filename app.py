from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/info')
def info():
    db_url = os.getenv('DB_URL', 'Not set')
    jwt_secret = os.getenv('JWT_SECRET', 'Not set')
    return jsonify({
        "db_url": db_url,
        "jwt_secret": jwt_secret
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)