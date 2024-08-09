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
                        def pylintOutput = sh(script: 'pylint . --exit-zero', returnStdout: true)
                        def match = pylintOutput =~ /Your code has been rated at ([0-9.]+)/

                        if (match) {
                            def pylintScore = match[0][1].toFloat()
                            echo "Pylint score: ${pylintScore}"

                            if (pylintScore < 8.0) {
                                error 'Pylint score is below 8! Failing the build.'
                            } else {
                                echo 'Passed linter!'
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
                    echo 'Running app for Tests'
                    try {
                        sh 'docker compose up --build'
                        sh 'docker compose exec server bash -c "PYTHONPATH=. pytest -s"'
                    } finally {
                        sh 'docker compose down'
                    }
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

        stage('Deploy') {
            steps {
                script {
                    sh 'echo Deploy'
                }
            }
        }
    }
}
