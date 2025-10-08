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

echo "Cleaning up old container if exists..."
# Check if a container is already using port 3200 and stop it
EXISTING_CONTAINER=$(docker ps -q --filter "publish=3200")
if [ ! -z "$EXISTING_CONTAINER" ]; then
    echo "Stopping existing container using port 3200..."
    docker stop $EXISTING_CONTAINER
    echo "Removing old container..."
    docker rm $EXISTING_CONTAINER
else
    echo "No existing container on port 3200."
fi

echo "Running new container from the latest image..."
docker run -d -p 3200:5000 --name jenkins_app_$BUILD_NUMBER ahsandc/jenkins-pipeline-test:$BUILD_NUMBER

echo "All done! Successfully deployed container version $BUILD_NUMBER"

exit 0
'''
      }
    }

  }
  environment {
    DOCKER_HUB_USERNAME = 'ahsandc'
    DOCKER_HUB_PASSWORD = 'Docker?12344321?dsa'
  }
}
