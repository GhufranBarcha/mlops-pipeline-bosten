pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/GhufranBarcha/mlops-pipeline-bosten.git'
            }
        }
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
        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: 'model.pkl', fingerprint: true
            }
        }
        stage('Deploy API') {
            steps {
                sh 'nohup python app.py &'
            }
        }
    }
}
