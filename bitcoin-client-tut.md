# Setting up our private bitcoin blockchain

This tutorial follows [[1]](https://bitcoin.org/en/developer-examples),
[[2]](https://bitcoin.org/en/developer-reference).

First of all, you need to install the bitcoin core client on your
computer. note that the bitcoin core client is actually three
programs: `bitcoind`, `bitcoin-qt`, and `bitcoin-cli`. the first is
the actual client, while the others are graphical and command line
interfaces. we'll be using only the first and last programs.

If you don't want to install the bitcoin core client directly, you can
follow the docker tutorial at [/docker/docker-tut.md](/docker/docker-tut.md) instead!  (it is
easier, but you'll have to
install [docker](https://www.docker.com/what-container) instead). if
you do, go to step 3 directly.

If you have questions, feel free to ask me (@odanoburu). please tell
me about any mistakes or possibilities of improvement!
   
1. Download the bitcoin core client:
   [[binaries]](https://bitcoin.org/en/download "bitcoin core download
   page") [[instructions]](https://bitcoin.org/en/full-node#linux-instructions) 
   [[source]](https://github.com/bitcoin/bitcoin)

	if you are using ubuntu, you can also install from a PPA (this is
   not recommended if you are going to use the real Bitcoin network):

        sudo add-apt-repository ppa:bitcoin/bitcoin
        sudo apt-get update
		sudo apt install bitcoind

2. Create a `bitcoin.conf` file in the application directory:

        Windows: %APPDATA%\Bitcoin\
                
        OSX: $HOME/Library/Application Support/Bitcoin/
                
        Linux: $HOME/.bitcoin/
	
	you may have to create the directory first (`mkdir
    $HOME/.bitcoin/`).

	the content should be the following
([see a template bitcoin.conf file if you like](https://github.com/bitcoin/bitcoin/blob/master/contrib/debian/examples/bitcoin.conf)):

		rpcuser=[PICK_USER]
		rpcpassword=[PICK_YOUR_PASSWORD]
		regtest=1

	the `regtest` variable saves us from having to specify the flag
`--regtest` for every command to `bitcoin-cli`.

3. Before we run the bitcoin node in our private bitcoin network, we
need to add a peer. ask for someone's IP, and run `bitcoind -regtest
-daemon -addnode=IP.ADDRESS:PORT`, substituting the person's IP
address and bitcoin client port. the default port for `regtest` mode
is 18444, if the person has changed that you should change it
too. **obs: everyone using docker is using a different port, default
is 4000.** note that the node you added might have to add you back
using `bitcoin-cli addnode "[IP.ADDRESS:PORT]" "add"`.

	The bitcoin core client will start running in the background.  we
	can now send RPC commands to `bitcoin-cli`.

	Try running `bitcoin-cli getblockchaininfo`. you should see your
	stats related to the regtest blockchain.
	
	Now try running `bitcoin-cli getpeerinfo`. see how many nodes you
    are connected to.

	**to stop the bitcoin client from running, type `bitcoin-cli
    stop`.**

	now run `bitcoin-cli help`. this summarizes some of the RPC
	commands available. a more complete reference is available at
	[[2]](https://bitcoin.org/en/developer-reference). `bitcoin-cli
	help [CMD]` will give you specific info about a certain command;

	note that the regtest blockchain offers some additional RPCs, such
	as `bitcoin-cli generate [nblocks]`, which creates nblocks out of
	thin air (which is obviously not possible in the traditional
	protocol). **obs: don't use this command in our private
	blockchain, else you can mess up the network's consensus by
	creating too many blocks too fast.**

4. Run `bitcoin-cli getnewaddress`. publish it to the course's online
   blackboard (check the README).

5. Check if your blockchain is synced by comparing the number of
   blocks between your peers. run `bitcoin-cli getblockcount`.
