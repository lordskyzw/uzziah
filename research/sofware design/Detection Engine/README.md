Detection Engine - Video pipeline

This folder contains a simple Python pipeline to run a video stream (webcam or file) against a PyTorch model saved at `resources/weights.pt`.

Files
- `pipeline.py`: main script. Usage examples below.
- `requirements.txt`: minimal Python dependencies (torch, opencv-python, numpy).

Quick start (PowerShell)

Install dependencies (adjust torch install for your CUDA or CPU environment):

python -m pip install -r requirements.txt


Run webcam (press q to quit):

python pipeline.py --source 0

Run an MP4 file and save output (preferred `--video` flag):

python pipeline.py --video "C:\path\to\video.mp4" --output "C:\path\to\out.mp4"

You can still use `--source` with a filepath, but `--video` is provided as a clearer alias for test MP4 files and will override `--source` when present.










# Detection Engine — Cleared

This folder was cleared per user request. The detection pipeline, frontend, tracking, and prediction components were removed and replaced with placeholder files.

If you want the pipeline restored, tell me which features to recreate (model loading, SORT tracking, Flask/SocketIO frontend, prediction thread), and I will re-implement them.
