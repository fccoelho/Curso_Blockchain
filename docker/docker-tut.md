# docker tutorial + alpine linux image tutorial

if you'd rather not install the bitcoin core client as in the
`bitcoin-testnet.md` tutorial, you can run it from a docker container
already set up -- although you will still need to download docker. you
can read more about docker
containers [here](https://www.docker.com/what-container).

1. get the docker community editon from
   the [docker website](https://docs.docker.com/engine/installation/).

2. check if docker is correctly installed: run `sudo docker run
   hello-world`. if you want to know what a command or flag does,
   `docker [CMD] --help` is your friend.

3. build the Dockerfile available on `/docker`: run `sudo docker build
   -t bitalpine [PATH-TO-DOCKERFILE]`. make sure to read it first!
   note that `bitalpine` is an arbitrary name to the container.

4. now run the image: `sudo docker run -it -p 18444:18444 --rm
   bitalpine /bin/ash`
		
	this should land you on the ash terminal of the alpine linux
    container.
