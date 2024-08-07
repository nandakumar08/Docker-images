pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('AKIAQEIP3RFFP65544GD') // Add AWS credentials in Jenkins
        AWS_SECRET_ACCESS_KEY = credentials('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')
        S3_BUCKET = 'githubtoawss3'
        GIT_REPO = 'https://github.com/nandakumar08/Docker-images.git'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: "${GIT_REPO}", branch: 'master'
            }
        }

        stage('Upload to S3') {
            steps {
                script {
                    sh """
                    aws s3 cp . s3://${S3_BUCKET}/ --recursive
                    """
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
