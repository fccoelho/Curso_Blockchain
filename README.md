# Cryptocurrencies and Blockchain

> **School of applied Mathematics - FGV**

Flávio Codeço Coelho

Introductory course on cryptocurrencies and other applications of blockchain technology.
This course is part of the Applied Maths and Data-Science Undergraduate programs of FGV

Video lectures (in portuguese) are available on [Youtube](https://www.youtube.com/watch?v=xqjow06qUEw), covering part of this course's content.

## News and announcements

> [**Online Billboard**](https://hackmd.io/EYUwhgrATAbFIFooAYCcyEBYAmaFlTiWFRGwgDMQKBmAdkyA?both)



| date       | conteúdo |
| ---------- | -------- |
| 2018-08-02 | leitura prévia do *white paper* para a aula (ver bibliografia) |
| 2018-08-09 | leitura prévia do paper [Raft](https://raft.github.io/raft.pdf) |

## Sylabus

1. Introdution to Bitcoin and its history; the origin of cryptocurrencies
2. Using Bitcoin Client
3. Cryptocurrencies: A global overview of the most important coins and how they work
3. Interacting with Bitcoin's blockchain from the Python console
4. Bitcoin's "Proof of Work". From concepts to practice.
1. Introduction to Cryptographic Hash functions and their use on Blockchains.
5. Eliptical Curve Cryptography and their use in Bitcoin.
    - RSA as a model of public key cryptography
6. Alt coins
7. [Proof of stake](https://en.wikipedia.org/wiki/Proof-of-stake).
8. The Ethereum platform and *smart contracts*.
9. Ethereum: White e Yellow paper
1. Understanding [Ethereum usage of Merkle Trees](https://blog.ethereum.org/2015/11/15/merkling-in-ethereum/)
10. [Desenvolvendo](/lectures/ethereum_dev.md) Aplicações na plataforma Ethereum
11. Introduction to the [Solidity Language](/lectures/Solidity.md)
12. Developing smart contracts: [Open-zeppelin](https://openzeppelin.org/).
1. Interacting with contracts from [Javascript](https://web3js.readthedocs.io/en/1.0/) and [Python](https://web3py.readthedocs.io/en/stable/).
13. Developping Decentralized Apps [(Dapps)](/lectures/dapp_meteor.md) using Meteor.

## Bibliography

### Bitcoin

- white paper [[pdf]](https://bitcoin.org/bitcoin.pdf) [[errata]](https://gist.github.com/harding/dabea3d83c695e6b937bf090eddf2bb3) [[HTML annotated]](https://genius.com/2683722) [[other formats]](https://github.com/karask/satoshi-paper)

- Mastering Bitcoin, Andreas Antonopoulos [[link]](http://chimera.labs.oreilly.com/books/1234000001802/index.html)

- developer documentation [[guide]](https://bitcoin.org/en/developer-guide) [[reference]](https://bitcoin.org/en/developer-reference) [[link]](https://bitcoin.org/en/developer-documentation)

- bitcoin para programadores [[pdf]](https://www.gitbook.com/download/pdf/book/itsriodejaneiro/bitcoin-para-programadores) [[repo]](https://github.com/BlockchainHub/bitcoin-para-programadores)


### Ethereum

- white paper [en](https://github.com/ethereum/wiki/wiki/White-Paper) [pt](https://github.com/ethereum/wiki/wiki/%5BPortuguese%5D-White-Paper) [PDF](/Ethereum-White-Paper.pdf)

- [Wiki](https://github.com/ethereum/wiki/wiki)
- [yellow paper](https://ethereum.github.io/yellowpaper/paper.pdf)
- [Beige paper](https://github.com/chronaeon/beigepaper)
- [Solidity Docs](http://solidity.readthedocs.io/en/latest/)
- [py-EVM](https://github.com/ethereum/py-evm)
- [Vyper](https://github.com/ethereum/vyper)
- [Auditing smart-contracts](https://medium.com/@merunasgrincalaitis/how-to-audit-a-smart-contract-most-dangerous-attacks-in-solidity-ae402a7e7868)

### Byzantine Fault Tolerant Protocols

- [Lamport, L et al. The Byzantine Generals Problem](https://www.microsoft.com/en-us/research/publication/byzantine-generals-problem/)

- [Lamport, L et al. The Part-Time Parliament](http://lamport.azurewebsites.net/pubs/lamport-paxos.pdf)

- Raft [[page](https://raft.github.io/)] [[paper](https://raft.github.io/raft.pdf)]
- [Generais bizantinos na Blockchain](https://docs.google.com/presentation/d/1hM2UPkStA0Xx73YC6SZnfGwsAxOTapgYLvB0EKBL9Jo/pub?start=false&loop=false&delayms=3000) 


### Other sources

- Bitcoin and Cryptocurrency Technologies (textbook) [[preprint](https://d28rh4a8wq0iu5.cloudfront.net/bitcointech/readings/princeton_bitcoin_book.pdf?a=1)] [[amazon](https://www.amazon.com/gp/product/0691171696/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0691171696&linkCode=as2&tag=jbonneau-20&linkId=59f35df2a92dd877cd22363bd8373a35)]

- bigchainDB whitepaper [[link]](https://www.bigchaindb.com/whitepaper/bigchaindb-whitepaper.pdf)

- Grin/MimbleWimble [[repo](https://github.com/ignopeverell/grin/)]

- permaCoin whitepaper [[link]](https://www.cs.umd.edu/~elaine/docs/permacoin.pdf)

- [Kosba, A et al. Hawk: The Blockchain Model of Cryptography and Privacy-Preserving Smart Contracts](https://eprint.iacr.org/2015/675.pdf)
- [Cryptoeconomics course](https://cryptoeconomics.study/)

### Proofs
Blockchains rely on different proving strategies to ensure distributed consensus. We will discuss some of them in this course.

#### Proofs of work

- [hashcash example](https://odanoburu.github.io/hash-cash)

- Ethereum Hash (Ethash) [[rationale](https://github.com/ethereum/wiki/wiki/Ethash-Design-Rationale)] [[spec](https://github.com/ethereum/wiki/wiki/Ethash)]

- cuckoo cycle [[pdf](https://github.com/tromp/cuckoo/blob/master/doc/cuckoo.pdf?raw=true)] [[repo](https://github.com/tromp/cuckoo)]

#### Proofs of Stake

- Casper (Ethereum proposal) [[non-triviality](https://blog.ethereum.org/2014/10/03/slasher-ghost-developments-proof-stake/)] [[repo](https://github.com/ethereum/research)] [[faq](https://github.com/ethereum/wiki/wiki/Proof-of-Stake-FAQ)]

- PeerCoin paper [[pdf](https://peercoin.net/assets/paper/peercoin-paper.pdf)]

#### Proofs of Retrievability

- [Juels, A et al. PORs: Proofs of Retrievability for Large Files](http://www.arijuels.com/wp-content/uploads/2013/09/JK07.pdf)

- [Bowers, K et al. Proofs of Retrievability: Theory and Implementation](http://dl.acm.org/citation.cfm?id=1655015)

#### Proof of Burn

- Slimcoin paper [[pdf](http://www.slimcoin.club/whitepaper.pdf)]



## Contributors
1. Bruno Cuconato @odanoburu
1. João Carabetta @JoaoCarabetta
