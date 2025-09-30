from flash import Flash, render_template, jsonify

app = Flask(__name__)

# App UI Route
@app.get("/")
def app_home():
    return render_template("app.html")

# Example API Route
@app.get("/api/hello")
def hello():
    return jsonify(ok=True, msg="Hello from Flask API")
