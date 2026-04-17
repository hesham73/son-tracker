from flask import Flask, request, render_template, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# تخزين آخر موقع تم استقباله
last_location = {"lat": None, "lng": None, "time": None}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update", methods=["POST"])
def update_location():
    global last_location
    data = request.json
    last_location = {
        "lat": data.get("lat"),
        "lng": data.get("lng"),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify({"status": "received"}), 200

@app.route("/map")
def show_map():
    return render_template("map.html", loc=last_location)

if __name__ == "__main__":
    # يعمل على الشبكة المحلية. للاستخدام الخارجي يحتاج Ngrok أو استضافة ويب
    app.run(host="0.0.0.0", port=5000, debug=True)