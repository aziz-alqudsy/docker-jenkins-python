# automated software testing using docker and jenkins
this is dummy project automation testing that integrated to jenkins and docker
tools :
- python 3.7
- pytest
- jenkins
- docker

## folder description
- jenkins-demo
  - src
    - __init__.py (an empty file which enables us to use this folder as a package)
    - calculator.py (functions that we test)
  - tests
    - test_addition.py (test add() fucntion from calculator.py)
  - DockerFile (setup docker to run test)
  - JenkinsDockerfile (setup docker to install jenkins for pipeline)
  - requirements.txt (to install dependencies)

## how to run
1. activate python virtual environment
   ```
   $ python -m venv venv
   $ source venv/bin/activate
   ```
2. extract and install dependencies
   ```
   $ pip freeze > requirements.txt
   $ pip install -r requirements.txt -U
   ```
3. build dockerize jenkins
   ```
   $ sudo su
   $ docker build -t jenkins-docker-image -f JenkinsDockerfile .
   ```
4. run container from jenkins-docker-image image
   ```
   $ docker run -d -p 8080:8080 --name jenkins-docker-container -v /var/run/docker.sock:/var/run/docker.sock jenkins-docker-image
   ```
5. open your jenkins in http://localhost:8080
6. get initial admin jenkins password for unlock jenkins page
   ```
   $ docker exec -it jenkins-docker-container cat var/jenkins_home/secrets/initialAdminPassword
   ```
7. create freestyle jenkins jobs
8. in Source Code Management tab, click on Git and add the repository URL. Enter the credentials by selecting Add->Jenkins and specifying the username and password of your Git account. This step will copy the repository python-test-calculator from the specified GitHub URL into /var/jenkins_home/workspace thereby creating the workspace inside our python-test-calculator directory.
9. Under Build tab, click on Add build step->Execute shell and copy the following:
   ```
   IMAGE_NAME="test-image"
   CONTAINER_NAME="test-container"
   echo "Check current working directory"
   pwd
   echo "Build docker image and run container"
   docker build -t $IMAGE_NAME .
   docker run -d --name $CONTAINER_NAME $IMAGE_NAME
   echo "Copy result.xml into Jenkins container"
   rm -rf reports; mkdir reports
   docker cp $CONTAINER_NAME:/python-test-calculator/reports/result.xml reports/
   echo "Cleanup"
   docker stop $CONTAINER_NAME
   docker rm $CONTAINER_NAME
   docker rmi $IMAGE_NAME
   ```
10. in Post-Build Actions tab, we specify the location in workspace of the copied result.xml for publishing. Ensure that JUnit plugin is installed on Jenkins. Save the project configuration.
11. click build now