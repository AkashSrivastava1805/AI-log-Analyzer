@Library("Shared") _
pipeline {
  agent { label "ghost" }

  environment {
    DOCKER_USER = "officialakashsrivastava"
    IMAGE_NAME  = "ai-log-analyzer"
    IMAGE_TAG   = "latest"
    NVIDIA_API_KEY = credentials('nvidia-api-key')
  }

  stages {

    stage("Code") {
      steps {
        script {
          code_clone("https://github.com/AkashSrivastava1805/AI-log-Analyzer.git","main")
        }
      }
    }

    stage("Build") {
      steps {
        script {
          docker_build(DOCKER_USER, IMAGE_NAME, IMAGE_TAG)
        }
      }
    }

    stage("Test") {
      steps {
        script {
          sh """
          docker run -d --name test-container \
            -e NVIDIA_API_KEY=${NVIDIA_API_KEY} \
            -p 5000:5000 \
            ${DOCKER_USER}/${IMAGE_NAME}:${IMAGE_TAG}
          """
          sh "sleep 10"
          sh "curl -f http://localhost:5000 || exit 1"
          sh "docker stop test-container"
          sh "docker rm test-container"
        }
      }
    }

    stage("Deploy") {
      steps {
        script {
          pushing_to_docker_hub(DOCKER_USER, IMAGE_NAME, IMAGE_TAG)
        }
      }
    }
  }
}
