pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/develop']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/amit-mainemer/PyFly.git']])
            }
        }

        stage('Lint') {
            steps {
                dir('server') {
                    sh "pylint ."
                }
            } 
        }

        stage('Tests') {
            steps {
                script {
                      sh "echo Test"
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh "echo build"
                }
            }
        }

        stage('Push Artifactory') {
            steps {
                script {
                   sh "echo Push Artifactory"
                }
            }
        }
    }
}
