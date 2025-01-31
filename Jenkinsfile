pipeline {
    agent {
        docker {
            image 'python:3.8-slim'
        }
    }
    environment {
        MODEL_PATH = 'models/xgboost_model.pkl'
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Train Model') {
            steps {
                sh 'python train.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ml-model:latest .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name ml-model-container ml-model:latest'
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
