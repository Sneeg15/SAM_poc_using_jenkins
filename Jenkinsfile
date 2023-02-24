pipeline {
    agent any 
    stages {
        stage('build') {
            steps {
                sh 'sam build'
            }
        }
        stage('deploy'){
            steps {
                sh 'sam deploy --no-confirm-changeset --no-fail-on-empty-changeset'
            }
        }
    }
}