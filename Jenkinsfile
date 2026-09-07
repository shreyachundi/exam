pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                echo 'Build the docker image'
                sh 'docker buid -t mypythonflaskapp .'
            }
        }
        stage('Run'){
            steps{
                echo 'Run the container'
                sh 'docker rm -f mycontainer || exit0'
                sh 'docker run -d -p 5004:5000 --name mycontainer mypythonflaskapp'
            }
        }
    }
    post{
        success{
            echo 'Docker pipeline successful'
        }
        failure{
            echo 'Docker pipeline failed'
        }
    }
}