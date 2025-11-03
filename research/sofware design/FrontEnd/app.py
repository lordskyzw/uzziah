from flask import Flask, render_template, jsonify, request
import threading
import time
import sys

app = Flask(__name__)

# Shared state placeholder for future video frames
shared_state = {
    "running": True,
    "last_frame_ts": None,
}


def video_thread():
    """Background thread placeholder for video processing / streaming.
    Currently it only updates a timestamp every second. Replace with
    real capture/encoding logic or socket emit when ready.
    """
    while shared_state["running"]:
        shared_state["last_frame_ts"] = time.time()
        # place to capture/process frames
        time.sleep(1)


@app.route('/')
def index():
    # Render front-end. The live feed area will show placeholder text.
    return render_template('index.html')


@app.route('/neutralize', methods=['POST'])
def neutralize():
    # This is where you will add the neutralize command. For now we print.
    print('neutralize', file=sys.stdout)
    sys.stdout.flush()
    return jsonify({"status": "ok", "action": "neutralize"})


if __name__ == '__main__':
    # Start background video thread (daemon so it exits with main process)
    t = threading.Thread(target=video_thread, daemon=True)
    t.start()

    # Run Flask app. In production use gunicorn or similar.
    app.run(host='0.0.0.0', port=5000, debug=True)


# ===== RUN INSTRUCTIONS =====
# 1. python3 -m venv venv && source venv/bin/activate
# 2. pip install Flask
# 3. project structure:
#    - app.py
#    - templates/index.html
#    - static/style.css
#    - static/script.js
# 4. python app.py
# 5. open http://localhost:5000

# Notes
# - The backend prints "neutralize" to stdout when the button is pressed.
# - Replace video_thread with real capture and a streaming mechanism later (WebSocket, MJPEG, WebRTC).
# - This UI uses a military aesthetic palette and a compact control column.
