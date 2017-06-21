# finding your way in the bitcoin client

after setting up our environment following the `bitcoin-client-tut.md`
tutorial, we can now explore the `bitcoin-cli` utility.

[[RPC commands
reference]](https://bitcoin.org/en/developer-reference#rpc-quick-reference)

from now on, we assume you have the `bitcoind` daemon running (`bitcoind
-regtest -daemon`).

## creating a transaction 

### the easy way

[ref](https://bitcoin.org/en/developer-reference#sendtoaddress)

	bitcoin-cli sendtoaddress "[address]" [value] [optional-comment]
	>> [result: transaction id, or tx-id]

this command will do everything for you under the hood: it will search
for UTXOs (unspent transaction outputs), select them according to some
criteria, then pick a suitable fee (again according to some criteria),
build the the scripts that allow the recipients to unlock the bitcoins
they received (following the default type of
transaction, [P2PKH](https://bitcoin.org/en/glossary/p2pkh-address)),
sign the transaction, and propagate it to other nodes.

all of this can be done manually, to a great degree of
customization. you can pick the exact UTXOs you want to spend, choose
the fee you want to pay (selecting a higher value for faster
confirmation, a lower value for a slower one, or even a value that is
so low that it probably will never be accepted by a miner, and the
transaction will never actually happen. you can even decide how the
bitcoins you paid can be unlocked: instead of paying to an address,
you can to whoever solves a puzzle, or even to the first person to
redeem the transaction output -- you just have to lear write it
in [*script*](https://en.bitcoin.it/wiki/Script), a non-turing
complete language which describes how UTXOs can be redeemed.

although we probably don't want or need such a degree of
customization, it is interesting to go into the details of how a
transaction is made, so that we can understand how Bitcoin works.

after running the previous command, we sent the transaction to other
nodes, so before the transaction gets added to a block in the
blockchain, it lives in nodes's *mempool*. it is from this memory pool
that valid transactions are drawn to form new blocks.

	bitcoin-cli getmempoolentry [txid]
	
will show us some information on the transaction referenced by [txid]
if it is in the mempool.

	bitcoin-cli gettransaction [txid]

will describe a transaction which was made by an address in our
wallet. **you should compare this output to**

	bitcoin-cli getrawtransaction [txid] 1

**which will display a transaction included in a block or in the
mempool.** the `gettransaction` RPC will show only the essential
information, and will do so in respect to you (e.g., the `amount` will
be positive or negative if you are receiving or spending
bitcoins). the `getrawtransaction` RPC will display the information as
it is stored on the blockchain, with all that this entails.

the second parameter `1` sets the output to verbose mode. the default
is `0`, which will display the serialized transaction instead of its
decoded version.

### the not-so-easy way

[ref](https://bitcoin.org/en/developer-reference#createrawtransaction)

	bitcoin-cli createrawtransaction '''
	[
		{
			"txid": "[txid]",
		"vout" : [tx-index]
			}
	]''' '{ "[address]": [value]}'

although this can be more troublesome to write, it is more
powerful. running `bitcoin-cli sendtoaddress "[address]" [value]` will
only send an amount to one person, and you can't specify from which
transaction this amount will come from.

using the `createrawtransaction` RPC, you can not only decide from
which UTXOs the money being sent will come from, but you can also send
it to several different addresses. go ahead, try it building such a
transaction.

**obs: the output will hex-encoded, so you'll need to run `bitcoin-cli
decoderawtransaction [hex-encoded-tx]` to see it in human readable terms.**

but remember this is the not-so-easy way. after runnning the
`createrawtransaction` RPC, you may have noticed that there are a few
missing values, compared to the output we got from
`sendtoaddress`. **which ones are they?**

now try sending this transaction using the `sendrawtransaction` RPC:

	bitcoin-cli sendrawtransaction [hex-encoded-tx]
	
you may have got the following error: `error message:256:
absurdly-high-fee`. **can you guess why?**

if you don't [[must set change address, else you'll pay the diff txin - txout as fees. go change the createrawtransaction!]]

we must sign its output. [[bitcoin-cli signrawtransaction, then sendrawtransaction]]
