# Assignment

# Solution
- You can run this application by running a docker image markfeher/mycv:1.0 like so:
```
docker run -e PORT=<PORT> -p <PORT>:<PORT> markfeher/mycv:1.0
```
> [!NOTE]
> You can choose what port will the Flask application inside the container listen on by specifying the PORT environment variable.
> i.e.: Following command will make the application run on port 8080 on your local VM, default is set to 3030: 

```
docker run -e PORT=8080 -p 8080:8080 markfeher/mycv:1.0
```

> [!NOTE]
> This containerized web CV was made with https://themes.3rdwavemedia.com/demo/bs5/risen/ bootstrap template.

The Docker build and push was automated by a Github Actions [workflow](https://github.com/mark-feher/myCV/blob/master/.github/workflows/docker-image.yml)

> [!NOTE]
> Testing whether workflow ignores README.md updates.

# Task 3

You will create a dedicated Kubernetes namespace, deploy the myCV application with three replicas, expose it via a NodePort service, and verify that the web application is reachable.

# Solution
![cluster_create.png]()
![create_namespace.png]()
![deployment.png]()
![mycv.png]()
