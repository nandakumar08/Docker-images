pipeline {
    agent (lable 'agentlinux')
  
    stages {
        stage("deploy") {
            steps {
                s3Upload consoleLogLevel: 'INFO', dontSetBuildResultonFailure: alse, dontwaitForConcurrentBuildCompletion: false, entries: [[bucket: jenkins-pipeline-s3', excludedFile: ", flatten: false, gzipFiles: false, keepForever: false, managedArtifacts: false, noUploadOnFailure: false, selectedRegion: 'ap-southeast-2, showDirectlyInBrowser: false, sourceFile: '/, storageClass: STANDARD', uploadFromSlave: false, useServerSideEncryption: false]], pluginFailureResultConstraint: 'FAILURE' , profileName: 'jenkinsfile' , userMetadata:[]                
            }
        }
    }
}
