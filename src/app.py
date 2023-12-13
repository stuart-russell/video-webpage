from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)

@app.route('/<video_id>')
def index(video_id):
    """
    Renders the index page for the specified video ID.

    Parameters:
        video_id (str): The ID of the video.

    Returns:
        str: The rendered index page with the embedded video URL.
    """
    embed_url = (
        f"https://www.youtube.com/embed/{video_id}"
        f"?autoplay=1&mute=1&controls=0&loop=1&playlist={video_id}"
    )
    return render_template('index.html', embed_url=embed_url)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=80)
