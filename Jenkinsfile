pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                script {
                    // Clone the repository
                    try {
                        git branch: 'main', url: 'https://github.com/whoami-anoint/Probe'
                    } catch (Exception e) {
                        echo "Error: Failed to clone repository - ${e.message}"
                    }
                }
            }
        }

        stage('Prepare') {
            steps {
                script {
                    // Download requirements.txt
                    try {
                        sh 'wget https://raw.githubusercontent.com/whoami-anoint/Probe/main/requirements.txt'
                    } catch (Exception e) {
                        echo "Error: Failed to download requirements.txt - ${e.message}"
                    }
                    
                    // Make shell scripts executable
                    try {
                        sh 'chmod +x make.sh probe.sh'
                    } catch (Exception e) {
                        echo "Error: Failed to chmod +x for shell scripts - ${e.message}"
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Run make.sh
                    try {
                        sh './make.sh'
                    } catch (Exception e) {
                        echo "Error: Failed to execute make.sh - ${e.message}"
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run probe.sh
                    try {
                        sh './probe.sh'
                    } catch (Exception e) {
                        echo "Error: Failed to execute probe.sh - ${e.message}"
                    }
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    // Clean up workspace
                    deleteDir()
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline has completed successfully!'
        }

        failure {
            echo 'Pipeline has failed!'
        }
    }
}
