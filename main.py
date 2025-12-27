from flask import Flask, redirect, Response
import requests
import os

app = Flask(__name__)

# --- CONFIGURATION ---
DNS = "https://dhoomtv.xyz"
USER = "P4B9TB9xR8"
PASS = "humongous2tonight"
HEADERS = {'User-Agent': 'IPTVSmartersPlayer'}

@app.route('/play/<stream_id>/index.m3u8')
def play_stream(stream_id):
    # Construct target URL
    target_url = f"{DNS}/live/{USER}/{PASS}/{stream_id}.ts"
    return redirect(target_url)

@app.route('/list')
def get_list():
    api_url = f"{DNS}/player_api.php?username={USER}&password={PASS}"
    try:
        r = requests.get(api_url, headers=HEADERS, timeout=10)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    # Wasmer Edge ke liye port 8080 default hota hai
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
