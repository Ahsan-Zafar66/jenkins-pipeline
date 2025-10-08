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
        sh '''echo "Current Directory:"
pwd
ls -l



echo "Building Docker image..."
docker build -t ahsandc/jenkins-pipeline-test:$BUILD_NUMBER .

echo "Logging in to Docker Hub..."
echo "$DOCKER_HUB_PASSWORD" | docker login -u "$DOCKER_HUB_USERNAME" --password-stdin

echo "Pushing image to Docker Hub..."
docker push ahsandc/jenkins-pipeline-test:$BUILD_NUMBER

echo "All done!"
'''
      }
    }

  }
  environment {
    DOCKER_HUB_USERNAME = 'ahsandc'
    DOCKER_HUB_PASSWORD = 'Docker?12344321?dsa'
  }
}