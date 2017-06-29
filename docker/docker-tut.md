# docker tutorial + alpine linux image tutorial

if you'd rather not install the bitcoin core client as in the
`bitcoin-client-tut.md` tutorial, you can run it from a docker
container already set up -- although you will still need to download
docker. you can read more about docker
containers [here](https://www.docker.com/what-container).

if you have questions, feel free to ask me (@odanoburu). please tell
me about any mistakes or possibilities of improvement!

1. get the docker community editon from
   the [docker website](https://docs.docker.com/engine/installation/).

2. check if docker is correctly installed: run `sudo docker run
   hello-world`. if you want to know what a command or flag does,
   `docker [CMD] --help` is your friend.

3. build the Dockerfile available on `/docker`: run `sudo docker build
   -t bitalpine [PATH-TO-DOCKERFILE-DIRECTORY]`. make sure to read it
   first!  note that `bitalpine` is an arbitrary name to the
   container.

4. now run the image: `sudo docker run -it -p 4000:18444 --rm
   bitalpine`
		
	this should land you on the ash terminal of the alpine linux
    container.
	
	(`4000` is an arbitrary port number that is bind to the 18444 port
    in the container, which is the port the bitcoin core client uses
    in `regtest` mode).
	
	to exit the terminal **and** the container, just type `exit`.

5. go back to step 3 in the `bitcoin-testnet.md` tutorial!
