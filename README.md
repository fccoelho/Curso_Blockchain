# Introdução às Criptomoedas e aplicações na Blockchain

> **Auditório 317, quintas-feiras às 14h.**

Flávio Codeço Coelho e Bruno Cuconato

Curso introdutório a Criptomoedas e outras aplicações da tecnologia da
Blockchain. Disciplina eletiva do Mestrado em modelagem matemática da
FGV. Uma série de vídeo-aulas seguindo o programa do curso está
disponível no [Youtube](https://www.youtube.com/watch?v=xqjow06qUEw).

## Avisos

quadro online da classe: [[link]](https://hackmd.io/EYUwhgrATAbFIFooAYCcyEBYAmaFlTiWFRGwgDMQKBmAdkyA?both)

**a partir do dia 20/07, teremos alguns seminários por aula sobre
alguma altcoin, à escolha do aluno. as escolhas devem constar no
quadro online da classe (acima ↑)**

| data       | conteúdo |
| ---------- | -------- |
| 2017-06-22 | leitura prévia do *white paper* para a aula (ver bibliografia) |
| 2017-06-13 | leitura prévia do paper [Raft](https://raft.github.io/raft.pdf) |

## Programa

1. Introdução ao Bitcoin e sua história
2. Usando o cliente bitcoin
3. Criptomoedas: o que são e como são usadas
3. Sessão prática interagindo com a tecnologia da Bitcoin usando Python
4. "Proof of Work" da bitcoin. Do conceito à pratica.
5. Curvas Elípticas e sua aplicação na Bitcoin.
    - RSA como modelo de public key cryptography
6. Alt coins
7. [Proof of stake](https://en.wikipedia.org/wiki/Proof-of-stake).
8. A plataforma Ethereum e os *smart contracts*.
9. Ethereum: White e Yellow paper
10. [Desenvolvendo](/lectures/ethereum_dev.md) Aplicações na plataforma Ethereum
11. Introdução à [linguagem Solidity](/lectures/Solidity.md)
12. Desenvolvendo contratos robustos: [Open-zeppelin](https://openzeppelin.org/).
13. Desenvolvendo aplicativos decentralizados [(Dapps) usando Meteor](/lectures/dapp_meteor.md).

## Bibliografia

### Bitcoin

- white paper [[pdf]](https://bitcoin.org/bitcoin.pdf) [[errata]](https://gist.github.com/harding/dabea3d83c695e6b937bf090eddf2bb3) [[HTML annotated]](https://genius.com/2683722) [[other formats]](https://github.com/karask/satoshi-paper)

- Mastering Bitcoin, Andreas Antonopoulos [[link]](http://chimera.labs.oreilly.com/books/1234000001802/index.html)

- developer documentation [[guide]](https://bitcoin.org/en/developer-guide) [[reference]](https://bitcoin.org/en/developer-reference) [[link]](https://bitcoin.org/en/developer-documentation)

- bitcoin para programadores [[pdf]](https://www.gitbook.com/download/pdf/book/itsriodejaneiro/bitcoin-para-programadores) [[repo]](https://github.com/BlockchainHub/bitcoin-para-programadores)


### Ethereum

- white paper [[en]](https://github.com/ethereum/wiki/wiki/White-Paper) [[pt]](https://github.com/ethereum/wiki/wiki/%5BPortuguese%5D-White-Paper)

- yellow paper [[link]](https://ethereum.github.io/yellowpaper/paper.pdf)

- Solidity Docs [[link]](http://solidity.readthedocs.io/en/latest/)

### Byzantine Fault Tolerant Protocols

- [Lamport, L et al. The Byzantine Generals Problem](https://www.microsoft.com/en-us/research/publication/byzantine-generals-problem/)

- [Lamport, L et al. The Part-Time Parliament](http://lamport.azurewebsites.net/pubs/lamport-paxos.pdf)

- Raft [[page](https://raft.github.io/)] [[paper](https://raft.github.io/raft.pdf)]
- [Generais bizantinos na Blockchain](https://docs.google.com/presentation/d/1hM2UPkStA0Xx73YC6SZnfGwsAxOTapgYLvB0EKBL9Jo/pub?start=false&loop=false&delayms=3000) 


### Outros

- Bitcoin and Cryptocurrency Technologies (textbook) [[preprint](https://d28rh4a8wq0iu5.cloudfront.net/bitcointech/readings/princeton_bitcoin_book.pdf?a=1)] [[amazon](https://www.amazon.com/gp/product/0691171696/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0691171696&linkCode=as2&tag=jbonneau-20&linkId=59f35df2a92dd877cd22363bd8373a35)]

- bigchainDB whitepaper [[link]](https://www.bigchaindb.com/whitepaper/bigchaindb-whitepaper.pdf)

- Grin/MimbleWimble [[repo](https://github.com/ignopeverell/grin/)]

- permaCoin whitepaper [[link]](https://www.cs.umd.edu/~elaine/docs/permacoin.pdf)

- [Kosba, A et al. Hawk: The Blockchain Model of Cryptography and Privacy-Preserving Smart Contracts](https://eprint.iacr.org/2015/675.pdf)

### Provas

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
