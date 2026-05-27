# Flask Kubernetes CI/CD Demo

This project is a simple Flask application packaged with Docker and prepared for deployment to Kubernetes. 
It also includes a GitHub Actions workflow that builds the Docker image and pushes it to DockerHub whenever changes are pushed to the `main` branch.

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
└── .github/workflows/workflow.yml
```

## Application

The Flask app exposes one route:

```text
GET /
```

It returns:

```text
GitHub Actions & Kubernetes Rolling Deployment Successful
```

The app listens on port `5000`.

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the app:

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

## Build and Run with Docker

Build the image:

```bash
docker build -t k2009dutta/flask-k8s-demo:v1 .
```

Run the container:

```bash
docker run -p 5000:5000 k2009dutta/flask-k8s-demo:v1
```

Open:

```text
http://localhost:5000
```

## Push Image to DockerHub

Log in to DockerHub:

```bash
docker login
```

Push the image:

```bash
docker push k2009dutta/flask-k8s-demo:v1
```

## Deploy to Kubernetes

The `deployment.yaml` file creates:

- A Kubernetes `Deployment` named `flask-k8s-demo`
- Two replicas of the Flask app
- A rolling update strategy
- A `NodePort` Service to expose the app

Apply the manifest:

```bash
kubectl apply -f deployment.yaml
```

Check the pods and service:

```bash
kubectl get pods
kubectl get svc flask-k8s-demo
```

For local testing, port forwarding is usually the simplest option:

```bash
kubectl port-forward service/flask-k8s-demo 5000:5000
```

Open:

```text
http://localhost:5000
```

If you are using a Kind cluster, make sure `kubectl` is using the Kind context:

```bash
kubectl config use-context kind-kind
```

## GitHub Actions CI/CD

The workflow in `.github/workflows/workflow.yml` runs on every push to `main`.

It performs these steps:

1. Checks out the repository
2. Logs in to DockerHub
3. Builds a Docker image
4. Pushes the image to DockerHub

The image is tagged with the Git commit SHA:

```text
k2009dutta/flask-k8s-demo:<github-sha>
```

## Required GitHub Secrets

Add these secrets in your GitHub repository settings:

```text
DOCKER_USERNAME
DOCKER_PASSWORD
```

`DOCKER_PASSWORD` can be a DockerHub access token.

## Notes

- The Docker image in `deployment.yaml` currently uses `k2009dutta/flask-k8s-demo:v1`.
- The GitHub Actions workflow pushes images tagged with `${{ github.sha }}`.
- To deploy a CI-built image, update `deployment.yaml` to use the pushed SHA tag or adjust the workflow to also push a stable tag such as `v1` or `latest`.
