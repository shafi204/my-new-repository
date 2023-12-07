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
              
              curl https://api.example.com/endpoint

          
              if curl -s --head https://api.example.com/endpoint | grep "200 OK" > /dev/null; then 
                echo "Endpoint is reachable"

              else
                echo "Endpoint in not reachable"
    
              time curl -o /dev/null -s -w "%[time_total]\n" https://api.example.com/endpoint
              }
} 
}
