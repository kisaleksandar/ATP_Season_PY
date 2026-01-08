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
            python -m venv venv 
            call venv/bin/activate
			python -m pip install --upgrade pip
            python -m pip install -r requirements.txt
            '''
            }
        }
    stage('Run Tests') {
        steps {
            bat '''
            call venv/bin/activate
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