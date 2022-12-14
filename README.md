# Machine-learning
First ML End to End Project

git add .
git commit -m 'messgae'
git push origin main
git status


build docker image

docker build -t <image_name>:<tagename>.

 <. stands for location as its a current location>
 <image name for the docker should be small>

 to list docker images command
   docker images

run docker image
   docker run -p 5000:5000 -e PORT=5000 5d9518d4e6d2

   5d9518d4e6d2-- this is image id of the docker

To check running container 
  docker ps
To Stop docker 
  docker stop <container id>