To run:

1. start selenium container
```
docker run --rm -it -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g seleniarm/standalone-chromium:latest
```
2. create credentials.yml
'''
username: YOUR_USERNAME
password: YOUR_PASSWORD
'''

3. map credentials.yml to docker-compose.yml
'''
volumes:
      - PLEASE_CHANGE_TO_PATH_IN_YOU_DIR/credentials.yml:/usr/project/credentials.yml 
'''

4. run docker compose command
'''
docker compose up
'''

In order to debug, can install VNC VIEWER and browse the section via:
localhost:5900 (default)

