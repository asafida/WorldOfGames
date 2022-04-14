pipelineTriggers([pollSCM('* * * * *')])])
node{
    stage("one"){
        git "https://github.com/asafida/WorldOfGames.git"
    } 
    stage("bla") {
    sh "ls -l"
    }
}
