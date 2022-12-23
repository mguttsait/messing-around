pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script{
                    sh "pwd"
                    sh "ls"
                    sh 'docker build -t mywebapp:latest .'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}