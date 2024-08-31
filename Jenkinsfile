pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'pyfly-repo-hub-cred'
        SSH_KEY_ID  = 'pyfly_ssh_key'
    }

    parameters {
        string(name: 'EC2_IP', defaultValue: '', description: 'The public IP of the EC2 instance')
    }

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
                dir('server') {
                    sh 'python3 -m venv venv'
                    sh 'venv/bin/pip install -r requirements.txt'
                    sh 'export FLASK_ENV=testing && export PYTHONPATH=$(pwd) && venv/bin/pytest . --maxfail=1'
                }
            }
        }

        stage('Build & Push images') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'echo $DOCKER_PASSWORD | sudo docker login -u $DOCKER_USERNAME --password-stdin'
                    }
                }
                dir('server') {
                    script {
                        sh 'docker build -t pyfly/pyfly_server:latest .'
                        sh 'sudo docker push pyfly/pyfly_server:latest'
                    }
                }
                dir('client') {
                    script {
                        sh 'docker build -t pyfly/pyfly_client:latest .'
                        sh 'sudo docker push pyfly/pyfly_client:latest'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sshagent([env.SSH_KEY_ID]) {
                        sh """
                        echo "Deploying to EC2 instance..."
                        ssh -o StrictHostKeyChecking=no ubuntu@${env.EC2_IP} \
                            'docker-compose down; docker container prune; docker rmi pyfly/pyfly_client:latest; docker rmi pyfly/pyfly_server:latest; docker-compose pull; docker-compose up -d'
                        """
                    }
                }
            }
        }
    }
}
