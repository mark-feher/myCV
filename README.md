# Assignment

# Solution
- You can run this application by running a docker image markfeher/mycv:1.0 like so:
```
$ docker run -e PORT=<PORT> -p <PORT>:<PORT> markfeher/mycv:1.0
```
> [!NOTE]
> You can choose what port will the Flask application inside the container listen on by specifying the PORT environment variable.
> i.e.: docker run -e PORT=8080 -p 8080:8080 markfeher/mycv:1.0 will make the application run on port 8080 on your local VM.
> Default is set to 3030.

> [!NOTE]
> This containerized web CV was made with https://themes.3rdwavemedia.com/demo/bs5/risen/ bootstrap template.
