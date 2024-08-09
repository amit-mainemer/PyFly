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
                    script {
                        sh 'pip install requirments.txt'
                        def pylintOutput = bat(script: 'pylint . --exit-zero', returnStdout: true)
                        def match = pylintOutput =~ /Your code has been rated at ([0-9.]+)/

                        if (match) {
                            def pylintScore = match[0][1].toFloat()
                            echo "Pylint score: ${pylintScore}"

                            if (pylintScore < 8.0) { // 8.0 corresponds to 80/100
                                error 'Pylint score is below 80! Failing the build.'
                            }
                        } else {
                            error 'Failed to parse pylint output!'
                        }
                    }
                }
            }
        }

        stage('Tests') {
            steps {
                script {
                    sh 'echo Running app for Tests'
                    sh 'docker compose up -d --build'
                    sh 'docker-compose exec server bash -c "PYTHONPATH=. pytest -s"'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'echo build'
                }
            }
        }

        stage('Push Artifactory') {
            steps {
                script {
                    sh 'echo Push Artifactory'
                }
            }
        }
    }
}
