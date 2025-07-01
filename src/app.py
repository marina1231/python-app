from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)


@app.route('/api/v1/details')

def details():
    return jsonify({
        'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'hostname': socket.gethostname(),
        'version': '1.0.0',
        'description': 'This is a sample Flask application for demonstration purposes.'
    })

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({
        'status': 'ok',
        'message': 'service is healthy',
        'version': '1.0.0' }), 200

# main driver function
if __name__ == '__main__':


    app.run()


#'/api/v1/details'
#'/api/v1/healthz'