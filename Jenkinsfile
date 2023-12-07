pipeline {
  agent any   
  stages {
      stage('Checkout') {
          steps
              checkout scm
          }
      }
      stage('Run Tests') {
          steps {
              
              curl https://jsonplaceholder.typicode.com/posts/1

          
              if curl -s --head https://jsonplaceholder.typicode.com/posts/1 | grep "200 OK" > /dev/null; then 
                echo "Endpoint is reachable"

              else
                echo "Endpoint in not reachable"
    
              time curl -o /dev/null -s -w "%[time_total]\n" https://jsonplaceholder.typicode.com/posts/1
              }
} 
}
