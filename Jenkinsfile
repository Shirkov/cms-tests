node {
    stage("Checkout repo"){
        git branch: 'master',
        credentialsId: '',
        url: 'https://github.com/Shirkov/cms-tests.git'
    }

    stage("Install deps") {
        sh 'pipenv install'
    }

    stage('Test') {
        sh 'pipenv run pytest src -sv --alluredir=allureresult'
    }


}