docker start hpc_docker
docker exec --user $USER -it hpc_docker /bin/bash

# optional stop container after done
# docker stop hpc_docker


### For documentation: Commands to create docker image and container hpc_docker
# cd /srv/dlc-shared/docker_dlc2182
# docker image build -t hpc_user/dlcdocker:2182 .
# docker run -v /home/hpc_user:/home/hpc_user -p 50804:22 -p 2351:8888 -e USER_GROUPS=sudo -e USER=hpc_user -e USER_ID=1002 -e USER_HOME=/home/hpc_user -e DISPLAY= -d --gpus all --name hpc_docker hpc_user/dlcdocker:2182
# docker exec --user $USER -it hpc_docker /bin/bash
# sudo apt update                                # inside container to fix cv2 issue
# sudo apt install ffmpeg libsm6 libxext6 -y     # inside container to fix cv2 issue
# 
# cd /usr/local/lib/python3.6/dist-packages/deeplabcut/pose_estimation_tensorflow/models/pretrained/
# sudo download.sh
# sudo chown hpc_user:hpc_user resnet_v1_50.ckpt      # resolve issue with permission denied for pretrained model

###
### Old script for nvidia-docker to create and start docker
###
# docker stop containername
# docker rm containername

# cd /srv/dlc-shared/Docker4DeepLabCut2.0
# GPU=0 bash ./dlc-docker run -d -p 2351:8888 -e USER_HOME=$HOME/projects-dlc/ --name containername mydlcuser:mydlcdocker
# docker exec --user $USER -it containername /bin/bash
