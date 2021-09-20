# Polkadot 

<img src="https://polkadot.network/assets/img/logo-polkadot.svg?v=e5bcd19e88" alt="logo" style="zoom:200%;" />



Web Site: https://polkadot.network/

Whitepaper: https://polkadot.network/PolkaDotPaper.pdf

Lightpaper: https://polkadot.network/Polkadot-lightpaper.pdf

## O que é Polkadot?

Polkadot é um protocolo open-source de compartilhamento multichain, permitindo que blockchains especializadas se comuniquem entre si em um ambiente seguro e confiável. Facilitando a transferência cross-chain de qualquer tipo de dado ou ativo, não apenas de tokens

Polkadot foi construído para conectar diferentes e proteger blockchains exclusivos, sejam eles públicos, rede "sem permissão", oráculos e futuras tecnologias,. Ele possibilita uma internet onde blockchains independentes podem trocar informações e transações sob garantias de segurança comuns.

Polkadot é uma rede viva com os pilares de governança e capacidade de atualização. A rede tem um conjunto avançado de ferramentas e governança, usando o padrão [WebAssembly](https://webassembly.org/) como um "meta-protocolo", pode implantar atualizações de rede de forma autônoma. Polkadot se adapta às suas necessidades crescentes sem os riscos de forks de rede.

Polkadot procura estabelecer uma rede totalmente descentralizada e privada, controlada pelos seus usuários, simplificando a criação de novas aplicações, instituições e serviços.

## Criação

Polkadot foi criada pela Web3 Foundation, uma Fundação Suiça. Os fundadores da Web3 são Dr. Gavin Wood, Robert Habermeier e Peter Czaban. Tem seu primeiro whitepaper publicado em outubro de 2016.

Wood o presidente da fundação, é o mais conhecido dos três, cofundador do Ethereum e criador da linguagem de codificação Solidity para smart contract. Habermeier pertence ao Thiel Fellow e realizou pesquisas e desenvolvimento de blockchain e criptomoedas. Czaban é o Diretor de Tecnologia da Web3 Foundation.

A polkadot foi criada com objetivo de transformar a internet em uma web descentralizada, onde os usuários controlam seus próprios dados e identidade em um ambiente trust-free. A Web3 visa remover intermediários e construir uma infraestrutura trustless (os participantes envolvidos não precisam se conhecer ou confiar uns nos outros ou em terceiros para que o sitema funcione).

## Como Funciona?

<img src="https://wiki.polkadot.network/assets/images/polkadot_relay_chain-c411a282aa36af0f20d04389919a6275.png" alt="arquitetura" style="zoom:40%;" />



### Arquitetura

Polkadot une uma rede de blockchains shards heterogêneas chamadas parachains. Essas chains  conectam-se e são protegidas pela Polkadot Relay Chain. Elas também podem conectar com redes externas via bridges.

#### Relay Chain

O "Coração" do Polkadot, responsável pela segurança da rede, consenso e cross-chain interoperabilidade.

#### Parachains

 Blockchains independentes que podem ter seus próprios tokens e otimizadas para casos de uso específicos. Para conectar com a Relay Chain, parachains podem pagar conforme vão alugar um slot para conectividade contínua.

#### Parathread

Semelhante ao parachains, mas com conectividade flexível, baseada em um modelo econômico de pagamento conforme utilização.

#### Bridges

Blockchains  especiais que permitem Polkadot shards(Parachains) se conectarem com blockchains externos como o Ethereum e o Bitcoin.

### Consensus Roles

#### Validators

Protegem a Relay Chain por staking DOT, validando as provas dos collators e participando em consenso com outros validators.

#### Collators

Mantêm parachains coletando transações de parachain de usuários  e produzindo provas para os validators.

#### Nominators 

Protegem a Relay Chain selecionando bons validators e fazendo o staking dos DOTs.

#### Fishermen

Monitora a rede e relata problemas de mau comportamento de validators. Collators e qualquer nó parachain completo pode realizar o papel do fisherman.

### Governance Roles

#### Council Member

Eleitos para representar stakeholder passivos em duas principais funções: propor referendos e vetar referendos perigosos ou maliciosos.

#### Technical Committee

Composto por equipes que estão desenvolvendo ativamente a Polkadot. Pode propor referendos de emergência, juntamente com o Council Member, para rápidas votaçoes e implementações.

## DOT Token

O token DOT serve para três propósitos distintos: governance, staking e bonding.

**Proof of Stake:** A ideia é que os  token holders possam manter moedas bloqueadas (seu valor de “stake”) e, a intervalos específicos, o protocolo atribui aleatoriamente a um deles, o direito de validar o próximo bloco. Geralmente, a probabilidade de um usuário ser selecionado para validação, é proporcional à quantidade de moedas em stake – quanto mais moedas, maior a probabilidade.

### Governance

Tolken holders (Portadores de tolkens) tem controle completo sobre o protocolo. Todos os privilégios, que em outras plataformas são exclusivos para mineiros, será entregue aos participantes Relay Chain  (DOT holders), incluindo gestão de eventos excepcionais como atualizações e correções de protocolo.

### Staking

A teoria dos jogos incentiva token holders a se comportarem de maneira honesta, seguindo as regras. Bons token holders são recompensados por este mecanismo e os maus perderão suas moedas bloqueadas (stake) na rede. Isso garante que a rede continue segura. Para ter mais detalhes sobre esse tipo de staking acesse : https://wiki.polkadot.network/docs/learn-staking.

### Bonding

Novos parachains são adicionados vinculando tokens. Já parachains desatualizados ou inúteis são removidos. Isto é uma forma de Proof of Stake.

## Algoritmo de Hash

O algoritmo de hash usado no Polkadot é a [Blake2b](https://en.wikipedia.org/wiki/BLAKE_(hash_function)#BLAKE2). Blake2 é considerada uma função hash criptográfica muito rápida que também é usada na [criptomoeda Zcash](https://z.cash/).

## Transações

A escabilidade teórica da rede em transações por segundo é de aproximadamente 1.000.000 plocamou Gavin Wood, porém a projeção de Polkadot é de cerca de 166.666 tps. Como Polkadot processa por meio de transações paralelas, o que permite, nos termos da Polkadot, 'escalabilidade infinita'. Não foi encontrado o número de tps atual.

## Emissão

Polkadot possui atualmente uma alocação de 1 bilhão de tokens DOT, em razão da [redenominação da rede](https://wiki.polkadot.network/docs/en/redenomination) de um fornecimento inicial máximo de 10 milhões em agosto de 2020. A redenominação ocorreu unicamente para evitar o uso de pequenas casas decimais e facilitar o cálculo. Embora todos os saldos tenham aumentado em um fator de cem, isso não afetou a distribuição do DOT ou a proporção detida pelos titulares.

DOT é inflacionária, não há um número máximo de DOT como  no Bitcoin. A inflação é projetada para ser de aproximadamente 10%ao ano, com recompensas do validador sendo uma função do valor  apostado ('staked') e o restante indo para tesouraria('treasury').

<img src="https://wiki.polkadot.network/assets/images/staking-participation-rate-da8419ef7f3e69baa73fa2009cc08cc0.png" alt="inflaction" style="zoom:80%;" />	

* **x-axis**: Proporção de DOT apostado('staked')
* **y-axis**: Inflação, porcentagem anualizada
* **Linha Azul**: recompensas da inflação para os stakers
* **Linha Verde**: Taxa de Retorno de Staker ('Staker rate of return')

O gráfico acima mostra o modelo de inflação da rede. Dependendo da participação do staking, a distribuição da inflação para validadores / nominadores versus o tesouro mudará dinamicamente para fornecer incentivos para participar (ou não) no staking.

## Smart-Contracts e outras aplicações específicas

A Relay Chain  da Polkadot não oferecera suporte nativo para smart contracts. No entanto, parachains em Polkadot vão suportar smart contracts. Já existem projetos anuciados como [Edgeware](https://edgewa.re/) , e graças ao Substrate contruído em [contract pallet](https://substrate.dev/rustdocs/latest/pallet_contracts/index.html), é provável que mais parachains suportem smart contracts WebAssembly.

Além disso, existe [EVM Pallet](https://substrate.dev/docs/en/knowledgebase/smart-contracts/evm-pallet), que permite uma parachain implemente a Máquina virtual da Ethereum, suportanto assim portas quase diretas de contratos Ethereum. Alguns dos projetos usam essa abordagem são [Edgeware](https://edgewa.re/) , [Moonbeam](https://moonbeam.network/) e [Frontier](https://github.com/paritytech/frontier) .

As parachains possibilitam a troca de qualquer tipo de dados entre diferentes tipos de blockchain, isso possibilita um mundo de diferentes casos.

## Curiosidades

* Os blockchains personalizados são rápidos e fáceis de desenvolver através da estrutura Substrate, e podem se conectar à rede Polkadot em poucos minutos. A rede também é altamente flexível e adaptável, permitindo o compartilhamento de informações entre os participantes, semelhante aos aplicativos para smartphones. A Polkadot pode ser atualizada automaticamente para implementar novos recursos ou remover bugs sem a necessidade de um fork.

- Kusama Network é uma rede não auditada e não refinada criada para testar tecnologia de rede e incentivos econômicos em um ambiente de mundo real. É um lugar perfeito para desenvolvedores de Parachains testar suas ideias antes de implementá-las na Polkadot. Kasuma é governada pela comunidade que possuem KSM tokens.



## Referências

https://coinmarketcap.com/pt-br/currencies/polkadot-new/

https://wiki.polkadot.network/

https://polkadot.network/Polkadot-lightpaper.pdf

https://polkadot.network/PolkaDotPaper.pdf

https://www.youtube.com/watch?v=2Gf7-tVuYFY

https://academy.binance.com/pt/articles/what-is-staking

https://cryptonews.com/coins/dot-polkadot/

























