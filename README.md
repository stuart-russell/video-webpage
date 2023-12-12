# Video Webpage

My main computer sucks and my work computer is a mac so running video wallpapers on either is a PITA. Luckily there are tools for MacOs and Windows that allow webpages to be set as a desktop background and so here we are.

This is a simple Flask webserver that will use a provided YouTube video ID to set the full page background. I can then set my desktop wallpaper to the correct URL and this is all handed off to my Raspberry Pi.

E.G. for some christmassy fun

`git clone git@github.com:stuart-russell/video-webpage.git`

`cd video-webpage`

Then either

`docker build -t video-webpage .`

`docker run -p 5000:5000 video-webpage`

Or

`poetry install`

`python src/app.py`

And open this page in your browser

`http://0.0.0.0:5000/Arwx8LLxlx8`
