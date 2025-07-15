# Python - Server-Side Rendering

**Tech to use**

- Docker
- SQLite
- Python
    - Flask
    - SQLAlchemy

## Usage
- Get the `Dockerfile` from the repo
- Run `docker build -t python-server_side_rendering .` @ the terminal to create the image
- Run `docker run --interactive --rm --tty --name CONTAINER_NAME python-server_side_rendering python` @ the terminal to create the container based on the image you just created `python-server_side_rendering`. At this very moment you only got Python. 
    - `--interactive` keep STDIN open so you can interact with the container NOTE: **You need to created interactive to interact later**
    - `--rm` flag remove the container at the moment you leave it
    - `--ty` flag gives you a usable shell
    - `--name` name the container


`docker run --interactive --detach --name python-server_side_rendering python-server_side_rendering python`