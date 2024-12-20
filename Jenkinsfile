pipeline {
    agent any
    
    environment {
        // Remember to replace with your Docker Hub username
        DOCKER_IMAGE = "your-dockerhub-username/webapp"
        DOCKER_TAG = "latest"
    }
    
    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }
        
        stage("Build") {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }
        
        stage("Push") {
            steps {
                script {
                    docker.withRegistry("", "docker-hub-credentials") {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                    }
                }
            }
        }
        
        stage("Deploy") {
            steps {
                sh "docker-compose down || true"
                sh "docker-compose up -d"
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
