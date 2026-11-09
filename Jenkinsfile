pipeline{
    agent any
    stages{
        stage('Build the Docker image'){
            steps{
                echo 'Build the docker image'
                sh 'docker build -t mypythonflaskapp .'
            }
        }
        stage('Run the container'){
            steps{
                echo 'Run the docker image'
                sh 'docker rm -f mycontainer || exit 0'
                sh 'docker run -d -p 5003:5003 --name mycontainer mypythonflaskapp'
            }
        }
    }
    post{
        success{
            echo 'The pipeline has completed successfully.'
        }
        failure{
            echo 'The pipeline has failed.'
        }
    }
}