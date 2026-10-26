pipeline{
    agent any
    stages{
        stage('Build docker image'){
            steps{
                echo "Build Docker image"
                sh 'docker build -t exam2:v1 .'
            }
        }
        stage("Login to docker hub"){
            steps{
                echo "Login to docker hub"
                sh 'docker login -u shreyachundi -p Karthikeya@011'
            }
        }
        stage('Push image'){
            steps{
                echo "Push the image to Docker Hub"
                sh 'docker tag exam2:v1 shreyachundi/exam:2image'
                sh 'docker push shreyachundi/exam:2image'
            }
        }
    }
    post{
        success{
            echo "Pipeline successful"
        }
        failure{
            echo "Pipeline failed"
        }
    }
}