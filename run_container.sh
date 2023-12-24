docker build -t rock_paper_scissors .
docker run -dp 8000:8000 --name rock_paper_scissors rock_paper_scissors
echo "Service avaiable at ip: "
docker inspect --format '{{.Name}} {{ .NetworkSettings.IPAddress }}' rock_paper_scissors  