pipeline {

    agent any
    
    environment {
        MODEL_PATH = 'models/xgboost_model.pkl'
    }
    stages {
        
        // stage('Train Model') {
        //     steps {
        //         sh 'python3 train.py'
        //     }
        // }

        stage('Push Docker Image to Artifact Registry') {
            steps {
                sh 'gcloud builds submit --region=region --tag us-central1-docker.pkg.dev/streamlit-app-kavindu/test-repo/test-image:latest .'
            }

        // stage('Build Docker Image') {
        //     steps {
        //         sh 'docker build -t ml-model:latest .'
        //     }
        // }
        // stage('Run Docker Container') {
        //     steps {
        //         sh 'docker run -d -p 5000:5000 --name ml-model-container ml-model:latest'
        //     }
        // }
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
