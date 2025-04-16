pipeline{
    agent any
    stages{
        stage("cloning"){
            steps{
                echo "pipeline is running"
                git url:"https://github.com/gowtham123K/priya.git",branch:'main'

            }
        }
        stage("dependency"){
            steps{
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install pytest
                '''
            }
        }
        stage("testing"){
            steps{
                bat '''
                    call venv\\Scripts\\activate
                    pytest test.py
                '''
            }
        }
        stage("deploy"){
            steps{
                bat '''
                    call venv\\Scripts\\activate
                    python login.py
                '''
            }
        }
    }
}
