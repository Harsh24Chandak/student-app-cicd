pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { git branch: 'main', url: 'https://github.com/Mayurk906/student-app-cicd.git' }
        }
        stage('Install & Test') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'python -m pytest -v'
            }
        }
        stage('Build Image') {
            steps { bat 'docker build -t student-app .' }
        }
        stage('Deploy') {
            steps {
                bat 'docker rm -f student-app-container || exit 0'
                bat 'docker run -d --name student-app-container -p 5000:5000 student-app'
            }
        }
        stage('Health Check') {
            steps {
                bat 'ping -n 6 127.0.0.1 > nul'
                bat 'curl http://localhost:5000/health'
            }
        }
    }
    post {
        success { echo 'Pipeline succeeded: student-app deployed on http://localhost:5000' }
        failure { echo 'Pipeline failed - check the stage logs above' }
    }
}
