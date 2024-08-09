pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/amit-mainemer/PyFly.git'
            }
        }

        stage('Lint') {
            steps {
                script {
                    def pylintResult = sh(script: 'pylint **/*.py || echo "pylint failed"', returnStatus: true)
                    if (pylintResult != 0) {
                        error "Pylint failed"
                    }
                } 
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def pytestResult = sh(script: 'pytest || echo "pytest failed"', returnStatus: true)
                    if (pytestResult != 0) {
                        error "Pytest failed"
                    }
                }
            }
        }


        stage('Deploy') {
            steps {
                script {
                    echo "push new images to hub"
                    echo "pull & restart my production env"
                }
            }
        }
    }
}
