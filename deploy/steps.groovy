#!groovy

def createConfig(def environment) {
  
  configFile = readYaml file: 'deploy/vars.yml'
  vars = configFile[environment]

  def config = [
          "INFRA_BUCKET=infraestructura.${environment}",
          "ENV=${environment}",
          "DEPLOY_REGION=${vars.DEPLOY_REGION}"
  ]

  return config
}

def showEnvironment(def config) {
    echo "Environment:"
    for(e in config){
        echo "--> ${e}"
    }
}

def build(def config) {
  withEnv(config) {
    sh 'make build.image'
  }
}

def deploy(def config) {
  withEnv(config) {
    sh 'make deploy'
  }
}

def update_service(def config) {
  withEnv(config) {
    sh 'make deploy'
  }
}

def delete_service(def config) {
  withEnv(config) {
    sh 'make delete'
  }
}

return this
