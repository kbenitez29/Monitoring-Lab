from flask import Flask
from prometheus_client import Counter, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST
from flask import Response

# Creating the server
app = Flask(__name__)

REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total app HTTP requests'
)

# Defining the route
@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return"""
    <div style="
        display: flex; 
        justify-content: center; 
        align-items: center; 
        height: 100vh; 
        margin: 0;
        font-family: Arial, sans-serif;
    ">
        <h1 style="font-size: 4rem; color: #2c3e50;">
            Greetings from ECS :)
        </h1>
    </div>
    """ # Defining the shown message

# Getting the metrics
@app.route('/metrics')
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )
@app.route('/health')
def health():
    return{"status": "ok"}, 200


# Accepting inbound traffic from the internet in HTTP port (ALB)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
