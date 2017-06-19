# Setting up our private bitcoin blockchain

this follows [1](https://bitcoin.org/en/developer-examples), [2](https://bitcoin.org/en/developer-reference).

1. download the bitcoin core
   client:
   [[binaries]](https://bitcoin.org/en/download "bitcoin core download page"), 
   [[source]](https://github.com/bitcoin/bitcoin).
   if you are using ubuntu, you can also install from a PPA (this is
   not recommended if you are going to use the real Bitcoin network):

        sudo add-apt-repository ppa:bitcoin/bitcoin
        sudo apt-get update
		sudo apt install bitcoind

2. create a `bitcoin.conf` file in the application directory:

        Windows: %APPDATA%\Bitcoin\
                
        OSX: $HOME/Library/Application Support/Bitcoin/
                
        Linux: $HOME/.bitcoin/

with the following content ([see the template bitcoin.conf file](https://github.com/bitcoin/bitcoin/blob/master/contrib/debian/examples/bitcoin.conf)):

> mkdir $HOME/.bitcoin/
>
> rpcpassword=PICK\_YOUR\_PASSWORD
>
> regtest=1

the second variable prevents us from having to specify the flag
`--regtest` for every command to `bitcoin-cli`.

3. now run `bitcoind -regtest -daemon`. the bitcoin core client will
start running in the background.  we can now send RPC commands to `bitcoin-cli`.

try running `bitcoin-cli getinfo`. you should see your bitcoind
version and stats related to the regtest blockchain.

now run `bitcoin-cli help`. this summarizes all the RPC commands
available. note that the regtest blockchain offers some additional
RPCs, such as `generate nblocks`, which creates nblocks out of thin
air (which is obviously not possible in the traditional protocol.

4. now we need to add other nodes to our regtest network. run
   `ifconfig` (or similar, if on Windows), and give us your IP
   address. add other people's nodes using
   the
   [`AddNode` RPC](https://bitcoin.org/en/developer-reference#addnode). syntax
   is IP-address:port, and the default port for the regtest network is
   18444.
   
   
        bitcoin-cli addnode "192.168.0.6:8333" "onetry"
