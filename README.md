# Student Registration App – CI/CD Pipeline and Monitoring

Mayur Khamamkar (DS 03, PRN 2324000146) · CSE (Data Science), Final Year B.Tech · A.Y 2026-27

A small Flask web app taken through the DevOps lifecycle on Windows. The tools are
Git (version control), GitHub (hosting), Docker (containerization) and Jenkins (CI/CD).
The app is monitored through its health/metrics endpoints, Docker stats/logs and Jenkins build history.

## Project structure
```
student-app-cicd/
├── app.py              # Flask routes: /, /api/students, /health, /metrics
├── templates/index.html
├── tests/test_app.py   # pytest test cases
├── pytest.ini
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── .dockerignore
└── .gitignore
```

## 1. Run locally (Windows cmd)
```
python --version
pip --version
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -v
python app.py              # open http://localhost:5000
```

## 2. Git and GitHub
```
git --version
git init
git status
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/Mayurk906/student-app-cicd.git
git branch -M main
git push -u origin main
git pull origin main
```

## 3. Docker
```
docker --version
docker compose version
docker info
docker build -t student-app .
docker run -p 5000:5000 student-app
docker ps
```

## 4. Jenkins
1. Install a JDK (17 or 21) and Jenkins LTS for Windows. Jenkins runs on http://localhost:8080.
2. Install the suggested plugins, including Git and Pipeline.
3. Make sure `python`, `git` and `docker` are on the PATH of the Jenkins service.
4. Create a new item "student-app-pipeline" of type Pipeline. Set Pipeline script from SCM, then Git, then this repo, with branch `main` and Script Path `Jenkinsfile`.
5. Click **Build Now**. The stages run in order: Checkout, Install & Test, Build Image, Deploy, Health Check.

```
java -version
git --version
docker --version
```

## 5. Monitoring
```
curl http://localhost:5000/health
curl http://localhost:5000/metrics
docker stats student-app-container
docker logs -f student-app-container
docker inspect student-app-container
```
In Jenkins, the Build History, Stage View and Console Output show each pipeline run.

## Endpoints
| URL | Purpose |
|---|---|
| `/` | Register students (HTML form) |
| `/api/students` | List registered students (JSON) |
| `/health` | Health check used by the Jenkins pipeline |
| `/metrics` | Request and student counters for monitoring |
