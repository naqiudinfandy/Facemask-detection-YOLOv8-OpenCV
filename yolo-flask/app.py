from flask import Flask, render_template, Response
from detector import detect, release_camera

app = Flask(__name__)

@app.route('/')
def index():
    """Render homepage with video feed"""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Route to display video stream"""
    return Response(detect(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/shutdown')
def shutdown():
    """Shutdown and release resources"""
    release_camera()
    return "Camera released."

if __name__ == "__main__":
    app.run(debug=True)
