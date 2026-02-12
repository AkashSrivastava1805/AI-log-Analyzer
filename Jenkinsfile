@Library("Shared") _
pipeline {
  agent {label "ghost"}
  stages {
    stage("Code"){
      steps{
        script{
          code_clone("https://github.com/AkashSrivastava1805/AI-log-Analyzer.git","main")
        }
      }
    }
    stage("Build"){
      steps{
        script{
          docker_build("officialakashsrivastava","ai-log-analyzer","latest")
        }
      }
    }
    stage("Test"){
      steps{
        script{
          sh "docker run -d -p 5000:5000 --env-file .env ai-log-analyzer:latest"
        }
      }
    }
    stage("Deploy"){
      steps{
        script{
          pushing_to_docker_hub("officialakashsrivastava","ai-log-analyzer","latest")
        }
      }
    }
  }
}
