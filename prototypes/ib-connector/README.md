# Getting Started
1. Build docker image
```bash
docker build -t <username>/ibconnector .
```

2. Create and start docker container
```bash
docker run -d -p 8080:8080 -v $(pwd):/app --name ibconnector <username>/ibconnector
```

3. Go to the [container's docs page](http://localhost:8080/docs) to interact with the API