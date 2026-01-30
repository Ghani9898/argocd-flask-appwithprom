from flask import Flask
from prometheus_client import make_wsgi_app, Counter
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNT = Counter('flask_request_count', 'Total HTTP Requests')

# Serve metrics on same port as Flask
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return "Hello, Flask!"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)