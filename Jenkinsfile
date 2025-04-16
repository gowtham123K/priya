pipeline{
    agent any
    stages{
        stage("cloning"){
            steps{
                echo "pipeline is running"
                git url:"https://github.com/gowtham123K/priya.git",branch:'main'

            }
        }
       stage("Compile Java Code") {
            steps {
                bat 'javac Calculator.java CalculatorTest.java'
            }
        }

        stage("Run Tests with Assertions") {
            steps {
                bat 'java -ea CalculatorTest.java'
            }
        }
    }
}

