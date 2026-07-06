from flask import Flask
from prometheus_client import start_http_server, Counter

app = Flask(__name__)
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc() # Sayacı 1 artır
    return "Gözlemlenebilirlik Projesi Canlı!"

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
