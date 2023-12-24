# Rock, Paper and Scissors
A simple api to learn how deploy an backend aplication on docker

## How to run
There are tree main methods:
1. Directly in the machine
2. Using shell script (brute force?)
3. Using docker compose (seems like a better option lol)

### Directly in the machine
In a world of distribuited micro services, running something in \
your own machine may seem out of dated, but you still can!
You should problably use some envelope so pip don't make a\
mess in your computer\
```pip install virtualenv```\
```virtualenv env```\
```source ./env/bin/activate```\
You are now running inside a isolated envelope.\
Proceed to download the dependencies\
```pip install -r requirements.txt```\
Finally, you can run your very own API\
```uvicorn main:app```


### Shell script
When deploying a docker container, you need to
* build image
* run container
The ```run_container.sh``` will do that for you \
To kill the service, run ```rm_container.sh```

### Compose
This more elegant approach does everything for you \
with just a ```docker compose up```
