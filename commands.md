docker build . -t prodexample -f .

docker run -p 5015:5005 -d prodexample

docker logs 'container_id'

docker container kill $(docker container ls -q)
