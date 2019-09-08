# Introduction to Hathor
In this lecture we will get acquainted with [Hathor Network](https://hathor.network). Hathor is a blockchain and criptocurrency 
platform, which seeks to deliver on the holy grail of transactions scalabitlity by combining the best of the Bitcoin proof-of-work
based consensus and fee-less transactions tipically associated with DAG-based blockchains. 

Throughout this lecture we will learn how to:
 - Download and setup a Hathor Wallet;
 - Set up you box to mine Hathors;
 - Create a new token 
 
## Start mining Hathors!
In order to start mining you first need to download the source code of the mining daemon and compile it locally. So far I have not found a pre-compiled miner ready for download and use. But compiling is not too complicated. Here I'll assume you will be doing it on an Ubuntu linux box like I did. Let's start with the [cpuminer](https://github.com/HathorNetwork/cpuminer). First clone the source code.

```bash
$ git clone https://github.com/HathorNetwork/cpuminer.git
```

The next step is to install some dependencies. Make sure you have performed the most basic step towards getting your OS ready to compile C code:

```bash
$ sudo apt install build-essentials
$ sudo apt install autoconf
```

Then you should install a could of libraries needed by the miner itself:
```bash
$ sudo apt install libcurl4-openssl-dev
$ sudo apt install libjansson-dev
```

Now you are ready to compile the cpuminer

```bash
$ ./autoge.sh
$ ./configure CFLAGS="-O3" # Make sure -O3 is an O and not a zero!
$ make
```
