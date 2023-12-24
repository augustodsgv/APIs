docker build -t rock_paper_scissors .
docker run -dp 8000:8000 --name rock_paper_scissors rock_paper_scissors
echo "Service avaiable at 127.0.0.1 (localhost) port 8000"