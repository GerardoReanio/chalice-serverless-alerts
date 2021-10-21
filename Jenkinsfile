def fnSteps = evaluate readTrusted("deploy/steps.groovy")

pipeline {
  agent any
  parameters {
    choice(
      name: 'ENVIRONMENT',
      choices: ['dev'],
      description: 'Ambiente donde se va a desplegar'
    )
    choice(
      name: 'EXECUTE',
      choices: ['DEFAULT', 'DEPLOY_STACK', 'UPDATE_SERVICE', 'DELETE_SERVICE'],
      description: 'Tarea a realizar'
    )
  }
  stages {
    stage('Set Config') {
      steps {
        script {
          echo '> Setting configurations ...'
          config = fnSteps.createConfig(
            params.ENVIRONMENT
            )
        }
      }
    }
    stage('Build') {
      when { expression { return params.EXECUTE == 'DEPLOY_STACK' || params.EXECUTE == 'UPDATE_SERVICE' }}
      steps {
        script {
          fnSteps.build(config)
        }
      }
    }
    stage('Deploy stack') {
      when { expression { return params.EXECUTE == 'DEPLOY_STACK' }}
      steps {
        script {
          fnSteps.deploy(config)
        }
      }
    }
    stage('Update service') {
      when { expression { return params.EXECUTE == 'UPDATE_SERVICE' }}
      steps {
        script {
          fnSteps.update_service(config)
        }
      }
    }
    stage('Delete service') {
      when { expression { return params.EXECUTE == 'DELETE_SERVICE' }}
      steps {
        script {
          fnSteps.delete_service(config)
        }
      }
    }
  }
  post {
    always {
      cleanWs()
    }
  }
}
