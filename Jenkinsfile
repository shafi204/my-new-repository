pipeline {
    agent any   
    stages {
        stage('Checkout') {
            steps  {
              checkout scm
          }
      }
      stage('Run Tests') {
          steps {
              sh 'curl https://jsonplaceholder.typicode.com/posts/1'

              script {
                  if (sh(script: 'curl -s --head https://jsonplaceholder.typicode.com/posts/1 | grep "200 OK" ', returnStatus: true) == 0) {
                      echo "Endpoint is reachable"

                  } else {
                      echo "Endpoint in not reachable"
                  }
              }
             
              sh 'time curl -o /dev/null -s -w "%[time_total]\n" https://jsonplaceholder.typicode.com/posts/1'
              }
} 
}
}
