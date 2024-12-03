pipeline {
    agent any

    environment {
        PROJECT_NAME = 'selenium_tests' // Define your project name
        HUB_PORT = '4444'          // Port for Selenium Hub
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Set up and Run Docker Compose') {
            steps {
                script {
                    // Ensure Docker Compose is installed on the Jenkins agent
                    sh 'docker-compose down || true' // Cleanup if already running
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the test container
                    sh 'docker exec ${PROJECT_NAME}_app-environment pytest'
                }
            }
        }

        stage('Teardown') {
            steps {
                script {
                    // Stop and remove all services after tests
                    sh 'docker-compose down'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        cleanup {
            script {
                sh 'docker-compose down'
            }
        }
    }
}
