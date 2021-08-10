# Creating a RESTful API with fastAPI, docker & postgres

As the title sugggests.

checkoiint failures

1. docker-compose installation
2. adding user to docker group

### Docker copose installation
'''https://docs.docker.com/compose/install/
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose'''


### Adding user to docker group
'''sudo gpasswd -a $USER docker
newgrp docker'''
