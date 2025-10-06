pipeline {
  agent any
  stages {
    stage('Git Clone') {
      steps {
        git(url: 'https://github.com/Ahsan-Zafar66/jenkins-pipeline', branch: 'main')
      }
    }

    stage('checking files') {
      steps {
        sh '''pwd
ls -l

docker --version
git --version

ls -la'''
      }
    }

  }
}