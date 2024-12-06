pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *') // Poll the Git repository every 5 minutes for changes
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/GhufranBarcha/mlops-pipeline-bosten.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv  # Create a virtual environment
                . venv/bin/activate   # Activate the virtual environment
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

    stage('Train Model') {
        steps {
            sh '''
            . venv/bin/activate   # Activate the virtual environment
            python3 train.py       # Run the training script
            '''
        }
    }


        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: 'model.pkl', fingerprint: true
            }
        }

    stage('Deploy Flask API') {
        steps {
            sh '''
            . venv/bin/activate && flask run # Run the Flask app
            '''
        }
    }
    }
}
