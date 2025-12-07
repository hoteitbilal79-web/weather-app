from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/weather")
def get_weather():
    
    city = request.args.get("city", "Beirut").strip()

  
    coords = {
        "beirut": (33.8938, 35.5018),
        "paris": (48.8566, 2.3522),
        "london": (51.5074, -0.1278)
    }

    lat, lon = coords.get(city.lower(), coords["beirut"])

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )

    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    # نرجع الحالي من الـ Open-Meteo
    return jsonify({
        "city": city,
        "latitude": lat,
        "longitude": lon,
        "current_weather": data.get("current_weather")
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
