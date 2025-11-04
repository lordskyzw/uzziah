from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO
import cv2, base64 # type: ignore
import threading
import time
import sys

app = Flask(__name__)
hmi_socket = SocketIO(app, cors_allowed_origins="*")  # allow connections from frontend

# Shared state placeholder for future video frames
shared_state = {
    "running": True,
    "last_frame_ts": None,
}


def video_thread():
    cap = cv2.VideoCapture(0)  # video source
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        # encode frame as JPEG and base64
        _, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer).decode('utf-8')
        # this is the actual emission
        hmi_socket.emit('video_frame', {'image': jpg_as_text})
        time.sleep(0.03)  # ~30 FPS


@app.route('/')
def index():
    # Render front-end. The live feed area will show placeholder text.
    return render_template('index.html')


@app.route('/neutralize', methods=['POST'])
def neutralize():
    # This is where we will add the neutralize command. For now we print.
    print('neutralize', file=sys.stdout)
    sys.stdout.flush()
    return jsonify({"status": "ok", "action": "neutralize"})



def run_flask():
    # Note: use debug=False in production
    hmi_socket.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=False)

if __name__ == '__main__':
    # Start background video thread (daemon so it exits with main process)
    detection_engine_thread = threading.Thread(target=video_thread, daemon=True)
    detection_engine_thread.start()

    # Start Flask in its own thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting Down Uzziah...")


