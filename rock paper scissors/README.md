# Rock, Paper and Scissors
A simple api to learn how deploy an backend aplication on docker

## How to run
There are two main methods:
1. Using shell script (brute force?)
2. Using docker compose (seems like a better option lol)

### Shell script
When deploying a docker container, you need to
* build image
* run container
The ```run_container.sh``` will do that for you \
To kill the service, run ```rm_container.sh```

### Compose
This more elegant approach does everything for you \
with just a ```docker compose up```