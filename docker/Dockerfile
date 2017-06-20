FROM alpine:3.6

# Set the working directory to $HOME
WORKDIR ~/

RUN apk --no-cache add bitcoin bitcoin-cli
RUN echo "regtest=1" >> /etc/bitcoin.conf
#RUN bitcoin-cli -conf=/etc/bitcoin.conf

# Make port 18444 available to the world outside this container
EXPOSE 18444