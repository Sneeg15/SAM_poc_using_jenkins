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
                sh 'sam deploy --stack-name sam-app -t template.yaml --s3-bucket sam-jenkins-demo-us-west-2-subhayandpwc --region us-east-1 --capabilities CAPABILITY_IAM --confirm-changeset true --image-repository docker-lambda-testapp' //--no-confirm-changeset --no-fail-on-empty-changeset'
            }
        }
    }
}
