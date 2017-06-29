# selecting the latest stable alpine linux image
# we're using alpine linux because its image is small (<10MB)
FROM alpine:3.6

# set the working directory to $HOME
WORKDIR ~/

# use alpine's package manager to download bitcoin and bitcoin-cli
# which are available
RUN apk --no-cache add bitcoin bitcoin-cli

# creating bitcoin.conf file
RUN mkdir ~/.bitcoin
RUN echo "regtest=1" > ~/.bitcoin/bitcoin.conf

# deleting alpine's built-in bitcoin client configuration
RUN rm /etc/bitcoin.conf
RUN rm /etc/init.d/bitcoin

# Make port 18444 available to the world outside this container. this
# is the default port used by bitcoin core client in regtest mode
EXPOSE 18444

CMD ["ash"]
