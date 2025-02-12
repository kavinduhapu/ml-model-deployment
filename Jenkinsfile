pipeline {

    agent {
      any
    }
    environment {
        MODEL_PATH = 'models/xgboost_model.pkl'
    }
    stages {
        
        // stage('Train Model') {
        //     steps {
        //         sh 'python3 train.py'
        //     }
        // }

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
