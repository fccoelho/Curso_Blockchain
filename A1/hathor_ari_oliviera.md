A1

# [Hathor Network](https://hathor.network/) <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNfYG_M1DERhKDPXiqD63kzTS9LSLqd0JTQb5nfWEGbrrDGtk_GSWsoRc262DfMr0Us-I&amp;usqp=CAU" alt="" width="33" height="33" class="jop-noMdConv" style="float: right;">


[con](#con)


## Uma blockchain escalonável e fácil de usar para ativos digitais


> A scalable distributed ledger for real-world applications.

[![Web Site](https://img.shields.io/badge/hathor-site-blue?style=for-the-badge)](https://hathor.network/) [![White Paper](https://img.shields.io/badge/white-paper-white?style=for-the-badge&logo=)](https://s3.amazonaws.com/hathor-public-files/hathor-white-paper.pdf) [![Source Code](https://img.shields.io/badge/source-code-green?style=for-the-badge&logo=github)](https://github.com/HathorNetwork) [![Python](https://img.shields.io/badge/python-love_%3C3-red?style=for-the-badge&logo=python)](https://www.python.org)

**A Hathor é uma plataforma digital para transações financeiras e contratos com o diferencial de combinar a alta escalabilidade e alta descentralização. Isso cria um ambiente perfeito para múltiplos casos de uso onde a escala, eficiência, segurança de longo prazo e resistência à censura por meio de distribuição da rede combinados são necessários ou podem ajudar a cortar custos de maneira drástica e evitar burocracias.**

> **Hathor is a digital platform for financial transactions and contracts with a unique combination of high scalability and high decentralization. It creates the perfect environment for multiple use cases where scale, efficiency, long-term security, and censorship-resistance through network distribution combined are needed or can drastically cut current costs and bureaucracy.**
> 
> * * *

### Pilares

1.  **Escalabilidade:** Taxa TPS na ordem de centenas contra as dezenas do ETH.
    
2.  **Usabilidade:** Acessível a leigos em programação.
    
3.  **Descentralização:** Maior liberdade e anonimato.
    
4.  **Sem taxas:** Sem custos e veloz.
    
5.  **Atomic Swaps:** Diferentes tokens podem ser trocados de forma confiável na mesma transação.
    
6.  **Nano Contracts:** Smart-contracts mais seguros e simples de se usar.
    

<center><img src="https://dchained.com/wp-content/uploads/2020/08/shutterstock_1517334278.png" class="jop-noMdConv" width="433" height="433"></center><center>Dos quais se destacam</center>

> [Landing page](https://landing.hathor.network/pt/hathornetworkbrasil) 
> 
> [Vídeo introdutório](https://youtu.be/OFSOcCybxk8)
> 
> * * *

## Concepção

## Criador brasileiro 🇧🇷

==A Hathor Network foi fundada em 2019== a partir da tese de doutorado do CTO ==Marcelo Salhab Brogliato== pela Fundação Getúlio Vargas (FGV), é uma nova arquitetura de consenso distribuída baseada em Proof-of-Work que usa estruturas de dados DAG e blockchain interligadas. Construída tendo em mente a escalabilidade, usabilidade e descentralização, a rede usa seu design inovador para resolver gargalos significativos que impedem a ampla adoção da tecnologia blockchain, além de diminuir as barreiras para desenvolvedores por conta de uma estrutura fácil de programação.

- ==A rede foi criada do zero, ou seja, não é um fork ou derivação de outros projetos.==
- ==Open Source==

> * * *

### Foco em escalabilidade

- Taxa ==TPS== na ordem de centenas contra as dezenas do ETH. Mas com capacidade para exceder as milhares de transações por segundo com as otimizações necessárias.
- Sendo a atual taxa de aproximadamente ==200 TPS==.

### Usabilidade

- Visa ser fácil/amigável para desenvolver

> “Até uma criança de 13 anos pode criar seu próprio token para se divertir.”

- Criação de tokens personalizados
    
- Para pessoas sem experiência com códigos(não precisa saber programar para criar seus tokens)
    
- Sem taxas
    
- Se vale do PoW da rede Bitcoin, logo pode aproveitar a estrutura já montada para minerar essa moeda, gastando assim menos energia e recursos, uma vez que, ao se minerar o HTR pode-se instantaneamente trocar por BTC.
    

> * * *

## Principais features

### Tokens personalizados

Você pode facilmente criar o seus próprio token para a sua aplicação de forma customizada e com apenas um click.

> [Vídeo explicativo](https://www.youtube.com/watch?v=Bcpn8eIbwdQ)

E funcionará baseado nas mesmas premissas da rede, ou seja, assumindo a alta escalabilidade e descentralização. Os tokens trabalham com cotação independente do preço de 1 HTR e podem ser usados para múltiplos propósitos:

- Como se fossem ações de uma empresa(finanças)
- Milhas ou pontos de fidelidade(comércio)
- Votações
- NFT’s e afins

### Nano Contracts

Uma versão mais simples dos Smart Contracts, onde os usuários podem transferir fundos para determinada transação através da rede Hathor caso determinado conjunto de regras ou ações se cumpram. De forma direta, esses contratos quando executados premiam os participantes de acordo com o que foi designado nas premissas iniciais, para tanto, existem os responsáveis por alimentar a rede com as informações necessárias para a validação(os Oráculos).

> Oracles are third party agents that submit pieces of information from the real world (outside of any blockchain) to inside the Hathor Network. For instance, if you want to bet your friend which team will win the match, you have to pick a trustworthy oracle that will say which team won.
> 
> * * *

## Arquitetura

A Hathor Network utiliza dois mecanismos em sua estrutura, o ==DAG==(Directed Acyclic Graph) e ==blockchain==, ou seja, é uma ==rede híbrida== baseada no Proof-of-Work do Bitcoin. A princípio tem semelhanças com a [IOTA](https://www.iota.org) por utilizar DAG, mas corrige uma falha grave que essa rede apresentava, que é a baixa performance quando o número de transações é baixo. Todavia, para contornar esse problema a IOTA desenvolveu uma espécie de agregador, que garante que as transações ocorram apesar de um eventual baixo uso da rede, porém, como se pode prever, tal medida mina a privacidade e possivelmente o anonimato dos envolvidos nas transações pois há esse garantidor que centraliza as operações. No DAG cada transação tem a sua própria *prova de trabalho* (PoW), que é resolvida pelo próprio emissor antes da transação ser propagada na rede. E também assim como no Bitcoin, os mineradores podem encontrar novos blocos que compõe a blockchain, só que dentro da DAG. Cada transação tem um peso acumulado que representam a quantidade de esforço empenhado para quebrar o bloco, semelhante ao número de confirmações no Bitcoin. Essa arquitetura híbrida permite uma grande escalabilidade advinda da DAG e descentralização pela blockchain, ou seja, garante também uma maior ==privacidade e real anonimato às operações==.

<center><img src="../../_resources/93a9c61349e4440ea206acb4386e9031.svg" alt="svgviewer-output.svg" width="279" height="466" class="jop-noMdConv">

*Representação simplificada da rede. Os blocos verdes são os componentes da blockchain. Os círculos brancos indicam os nós da DAG.*

</center>

Desse modo, a título de comparação podemos considerar que a Hathor é um misto das redes IOTA, Constellation e Bitcoin, sendo essa última a mais importante em semelhanças técnicas, ou seja, a Hathor assim como o Bitcoin utiliza o SHA-256 como função hash, permitindo assim a mineração mesclada de ambas as criptos. ==Essa mescla de tecnologias é o diferencial principal da rede==, pois agrega os melhores pontos de cada uma delas e corrige as suas deficiências.

<center><img src="https://coinmetro.com/blog/wp-content/uploads/2021/04/hathor.jpg" class="jop-noMdConv" width="312" height="385">

*Representação detalhada da rede com transações e blocos. As caixas vermelhas são os blocos; os balões verdes são as transações confirmadas; os balões brancos são as transações que estão ocorrendo; os amarelos são transações ainda não confirmadas; e os cinzas são transações resolvendo o PoW e que ainda não foram propagadas. As setas mostram o fluxo. As setas em destaque pertencem aos blocos.*

</center>

### Merged mining

> Mineração mesclada: utiliza o PoW com o mesmo algoritmo do Bitcoin(==sha256d==)
> Interoperabilidade com a blockchain do Bitcoin

Os mineradores encontram novos blocos que pertencem à blockchain dentro da DAG. Isso assegura que a rede continue funcionando mesmo que o número de transações por segundo esteja baixo. Os blocos coletam os tokens recém-gerados e confirmam todas as transações na DAG.

Agora olhando do ponto de vista prático, o Bitcoin é a mais robusta e segura blockchain, pois há uma vasta rede de usúarios que possui grande poder computacional agregado. Então os mineradores de HTR têm a vantagem de poder se aproveitar da infraestrutura já existente para a mineração de BTC e utilizá-la para adquirir HTR. E essa mescla de mineração é vantajosa até para quem tem interesse exclusivamente em BTC, pois se pode fazer a troca HTR->BTC instantaneamente sem custos extras, e também no sentido de que o retorno absoluto de se minerar HTR é menor.

> Merged mining with Bitcoin, hashrate all-time-high at 1.2EH/s

O merged mining também é visto na arquitetura do Dogecoin, que tem mineração compartilhada com o Litecoin.

### Tokenização

Para criar um token personalizado você apenas precisa preencher um simples formulário e já terá ele à sua disposição para uso. Não é necessário lidar com programação ou outros aspectos técnicos de blockchains. E os casos de uso são inúmeros, um exemplo é a [9Block](https://9block.com.br) empresa de NFT do Felipe Neto que se baseia na rede Hathor.

> https://beincrypto.com.br/felipe-neto-plataforma-nft-blockchain-hathor/

<center><img src="https://thegarret.org.uk/wp-content/uploads/2021/06/WhatsApp-Image-2021-06-10-at-10.07.17.jpg" class="jop-noMdConv" width="309" height="195"></center><center>Uma exemplo prático de como é fácil usar a Hathor Network. Se até o Felipe Neto consegue fazer um token personalizado, você também consegue. *contém ironia*</center>

### Ponto de vista financeiro

Uma pergunta pertinente a se fazer é:

> **A Hathor será valiosa no futuro?**

A resposta segundo os desenvolvedores é que sim, pois a rede não se restringe a casos de uso específicos, tokens e produtos podem ser criados e lançados na Hathor Network globalmente. Os tokens Hathor são divididos em duas classes, os pré-mineirados e os disponíveis para a mineiração.

- **Pré-mineirados**: Há ==um bilhão== de tokens já mineirados do primeiro bloco construído, e eles estão sujeitos a `burn`, estocagem e ao bloqueio programado. Tais medidas visam regular a inflação do HTR.

> Os tokens estocados estão reservados por um período de 5 anos desde a criação, e estarão disponíveis em 03/01/2025. A Hathor irá reavaliar esses tokens e passa-los adiante se fizer sentido para o crescimento e suporte da rede, caso contrário eles serão destruídos parcial ou completamente.

- **Mined tokens**: São gerados continuamente em todo bloco como uma recompensa para os mineradores por manterem a rede segura. A média de tempo entre os blocos é de 30 segundos. Atualmente cada bloco fornece 64 HTR como recompensa. E esses tokens estão sujeitos ao **halving**, que é o corte à metade para as recompensas, com a última ocorrendo em Janeiro de 2021.

Depois de `Janeiro de 2023` a quantidade de tokens por bloco será constante e igual a 8 HTR, e a taxa de inflação será abaixo de 1.1% descrecendo a cada ano.

> O crescimento da oferta de HTR está sujeito às recompensas da mineração e à sua taxa de inflação.

## Como começar a operar HTR?

Primeiros passos:
> https://hathor.network/get-started/

Para quem deseja minerar:
> https://hathor.network/resources/mining-tools/


> Referências: 
> 
> http://kyc.co/hathor-network/ 
> 
> https://teckers.com/hathor-network/ 
> 
> https://hathor-public-files.s3.amazonaws.com/hathor-token-economics.pdf 
> 
>  https://medium.com/hathor-network

* * *

<center><img src="https://hathor.network/theme/img/hathor-logo-black.png" alt="https://medium.com/hathor-network" class="jop-noMdConv" width="159" height="40"></center>