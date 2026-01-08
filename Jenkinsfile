pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/kisaleksandar/ATP_Season_PY.git'
            }
        }
    stage('Setup'){
        steps {
            bat '''
            python3 -m venv venv 
            source venv/bin/activate
            pip install -r requirements.txt
            '''
            }
        }
    stage('Run Tests') {
        steps {
            bat '''
            source venv/bin/activate
            pytest --junitxml=results.xml
            '''
        }
        post {
            always {
                junit 'results.xml'
            }
        }
    }
  }
}