pipeline {
    agent { label 'windows-docker' }

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Validar y construir') {
            steps {
                bat '''
                    if not exist .env copy .env.example .env
                    set "COMPOSE_PROJECT_NAME=entrega1-jenkins-%BUILD_NUMBER%"
                    docker compose config --quiet
                    docker compose build python-app
                '''
            }
        }

        stage('Prueba de integración') {
            steps {
                bat '''
                    set "COMPOSE_PROJECT_NAME=entrega1-jenkins-%BUILD_NUMBER%"
                    docker compose up -d redis
                    docker compose run --rm python-app
                '''
            }
        }
    }

    post {
        always {
            script {
                bat(
                    returnStatus: true,
                    script: 'set "COMPOSE_PROJECT_NAME=entrega1-jenkins-%BUILD_NUMBER%" && docker compose down --volumes --remove-orphans'
                )
            }
        }
    }
}
