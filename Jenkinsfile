pipeline {
    agent any

    environment {
        PROJECT_NAME = 'selenium_tests'         // Define your project name
        HUB_PORT = '4444'                      // Port for Selenium Hub
        GRID_TIMEOUT = '30'                    // Timeout for Selenium Grid
        GRID_MAX_SESSION = '10'                // Max sessions for Selenium Grid
        ENV_FILE = './environment/Dev.env'     // Path to environment file
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the GitHub repository
                checkout scm
            }
        }

        stage('Set up and Run Docker Compose') {
            steps {
                script {
                    // Ensure Docker Compose is installed on the Jenkins agent
                    sh '''
                        docker-compose down || true        // Cleanup any existing services
                        docker-compose up -d              // Start services in detached mode
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Execute tests inside the app environment container
                    sh "docker exec ${PROJECT_NAME}_app-environment pytest"
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
            script {
                // Ensure all services are stopped
                sh 'docker-compose down || true'
            }
        }
    }
}
