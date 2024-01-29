pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Checkout the code from the GitHub repository
                git 'https://github.com/whoami-anoint/your-repo.git'
            }
        }
        stage('Build') {
            steps {
                // Your build commands or scripts go here
                sh 'echo "Building the project"'
            }
        }
        stage('Test') {
            steps {
                // Your testing commands or scripts go here
                sh 'echo "Testing the project"'
            }
        }
        stage('Deploy') {
            steps {
                // Your deployment commands or scripts go here
                sh 'echo "Deploying the project"'
            }
        }
    }

    post {
        always {
            // Cleanup steps, if any
            echo 'Pipeline execution finished'
        }
    }
}
