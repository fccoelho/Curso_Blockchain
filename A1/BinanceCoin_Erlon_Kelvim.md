# Binance Coin (BNB)

<img src="https://portaldobitcoin.uol.com.br/wp-content/uploads/2021/04/shutterstock_1876433254.jpg" style="width: 433px; height: 260.684px; margin: 6.60816px 0px;">


## Sumário

1. [O que é a Binance Coin?](#1)
2. [Mecanismo de consenso](#2)
3. [Design criptográfico](#3)
4. [Referências](#4)

<a id='1'></a>

## O que é a Binance Coin?
É possível encontrar o Whitepaper da Binance no endereço [Whitepaper Binance](https://web.archive.org/web/20200422153723/https://www.binance.com/resources/ico/Binance_WhitePaper_en.pdf) O Whitepaper da BSC no endereço [Whitepaper BSC](https://github.com/binance-chain/whitepaper/blob/master/WHITEPAPER.md) e o site da binance [aqui](https://www.binance.org/pt)

A Binance Coin (BNB) é a criptomoeda nativa da Binance Smart Chain (BSC), que por sua vez é controlada pela Binance. Assim sendo, antes de qualquer coisa é importante conhecer a Binance. Atualmente, a Binance é a maior Exchange (ou seja, bolsa de criptoativos) do mundo em volumes transações. Foi fundada, em 2017, por Changpeng Zhao e inicialmente era sediada na China, mas, devido ao aumento de regulação feita pelo governo chinês, transferiu sua sede para o Japão. Além disso, a Binance Exchange possui uma das maiores variedades de criptoativos e uma das menores taxas de negociações do mundo, estando presente em diversos países.
Simultaneamente à fundação da Binance, houve a criação da Binance Coin como um token ERC-20 na blockchain da Ethereum, com o objetivo de permitir aos seus usuários realizar transações com uma taxa mais baixa do que utilizando outros tokens. Em um processo de Initial Coin Offering (ICO), a Binance ofereceu 10% das suas 200 milhões de BNBs para investidores-anjos, 40% para seus fundadores e 50% para o público em geral. Uma das caracteísticas da BNB é a reaização do processo de "queima", onde a Binance utiliza o lucro advindo da venda de tokens para comprar Binance Coins e destruí-las, diminuindo a quantidade de BNBs em circulação e, consequentemente, apreciando-as. Esse processo de queima de Binance Coins não ocerrerá infinitamente, sendo limitado a 50% das BNBs que foram colocadas em circulação durante seu ICO. Além disso, não é possível emitir novas Binance Coins, de modo que eventualmente (ao final do processo de queima) a quantidade total de BNBs será 100 de milhões de tokens, confirurando-a como uma moeda deflacionária. Outro ponto é que a BNB possui interoperabilidade com outras Bloclchains.
A Biticoin possui altas taxas de negociação e problemas de escalabilidade por bloco, sendo sua principal função a de reserva de valor, assim como o ouro. Por outro lado, a Binance Coin foi criada com o objetivo de ser um token utilitário e realmente desempenhar funções semelhantes (mas não limitadas) às de uma moeda fiduciária. Os usos da BNB incluem: a Binance Coin poder ser negociada por outras criptomoedas em várias bolsas, dependendo das restrições definidas pela bolsa; os usuários da Binance Exchange recebem um desconto ao usar BNB para pagar por suas transações; Binance Coin pode ser a forma de pagamento para contas de cartão de crédito criptografado em crypto.com; os estabelecimentos comerciais podem aceitar Binance Coin como meio de pagamento, oferecendo mais flexibilidade aos clientes; é possível, em sites selecionados, reservar hotéis e voos com BNB; diversas plataformas permitem que o investimento em ações, ETFs e outros ativos usando Binance Coin; é possível usar BNB como garantia para empréstimos em determinadas plataformas; também existem aplicativos que permitem aos usuários dividir contas e pagar terceiros com Binance Coin. Além disso a BNB pode ser fracionada em até 8 casas decimais, permitindo negociações de valores pouco significativos e assegurando sua utilidade em transações do dia-a-dia.
Em setembro de 2020 a Binace anunciou a Binace Smart Chain (BSC), sua nova plataforma DeFi. A BSC foi lançada posteriormente, em abril, oferecendo uma alternativa às outras plataformas DeFi (como Ethereum, Cardano, dentre outros) e fornecendo compatibilidade cross-chain com a Binance Chain, com o objetivo de introduzir _smart contracts_ em seu ecossistema, sem prejudicar o alto rendimento da Binance Chain. Além disso, a BSC oferece suporte para outras criptomoedas e facilita a migração dos projetos pelos desenvolvedores da blockchain Ethereum para ela.

<a id='2'></a>

## Mecanismo de consenso

A BSC introduziu um novo conceito de consenso, a Proof of Staked Authority (PoSA). A PoSA combina o melhor da Proof-of-Authority (PoA) e da Delegated Proof of Stake (DPoS), ela conta com 21 validadores e proporcionam um menor tempo de geração de blocos e uma taxa de transação mais baixa.
Os blocos são produzidos por um número limitato de validadores, mais especificamente 21, que se revezam para produzir os blocos da maneira PoA. Além disso, diariamente há uma reeleição dos validadores com base na staking governance para participar do conjunto de validadores.
Existem dois tipos de validadores, os validadores candidatos, que são aqueles que cumprem os requisitos mínimos de Hardware, executando um hardware node e tendo um self-stake mínimo de 10.000 BNB. Já os validadores eleitos são os 21 validadores que possuírem o maior volume de BNB delegado (self-stake + delegators’ stake). 
Os delegadores são aqueles que fazem staking de BNB para os validadores candidatos através de uma carteira suportada, eles podem votar em seus validadores preferidos e ajudá-los a atingir o valor mínimo para se tornar um validador eleito. 
Esse processo é lucrativo para ambos os lados pois os validadores recebem uma recompensa em BNB para validarem os blocos, mas em compensação divide parte do seu lucro com os delegadores em troca do "voto de staking".
Esse tipo de consenso faz com que, apesar de ser um processo descentralizado, já que os validadores podem ser trocados de acordo com o staking popular, se restrinja a um um grupo restrito de validadores na execução dos blocos. Ou seja, tem a vantagem de ser mais rápido e barato, mas possui a desvantagem de ser menos descentralizado do que outras criptomoedas, como o Bitcoin.

<a id='3'></a>

## Design criptográfico

Para usuários normais, todas as chaves e endereços podem ser gerados via Binance Web Wallet.
Esta carteira-padrão usa uma maneira semelhante ao Bitcoin para gerar chaves, ou seja, usa entropia de 256 bits para gerar um mnemônico de 24-word baseado em BIP39, e então usa o mnemônico e uma frase-senha vazia para gerar uma seed e, finalmente, usando a seed para gerar uma chave-mestra e derivar a chave-privada usando BIP32/BIP44 com o prefixo HD como "44'/714'/", que é reservado em SLIP 44 .
A Binance Chain usa a mesma criptografia de curva elíptica presente na execução da Bitcoin, ou seja secp256k1. Sua chave-privada é de 32 bytes, enquanto a chave-pública é de 33 bytes.
Os endereços na cadeia da Binance normalmente têm 20 bytes e possuem um endereço é codificado no formato bech32, que, por sua vez, inclui uma soma de verificação e um prefixo legível por humanos (HRP). Entretanto, ele não usa o formato de endereço SegWit.
Um endereço Binance Chain é, portanto, mais semelhante a um endereço Bitcoin Cash, que, por sua vez, não inclui um script de programa SegWit. A Cadeia Binance usa uma assinatura ECDSA na curva secp256k1, ao invés de um hash SHA256 da matriz de bytes de uma representação canônica codificada em JSON da transação.

<a id='4'></a>

## Referências

- https://academy.binance.com/pt/articles/a-quick-guide-to-bnb-staking-on-binance-smart-chain-bsc
- https://corporatefinanceinstitute.com/resources/knowledge/other/binance-coin-bnb/
- https://docs.binance.org/
- https://docs.binance.org/blockchain.html
- https://www.binance.org/en/blog/a-journey-to-decentralization-validators-delegators/
- https://www.thestreet.com/crypto/defi/what-is-binance-coin-is-it-a-good-investment

