# Litecoin (LTC)
> A prata das criptomoedas 

<img src="https://blog.flashift.app/wp-content/uploads/2021/08/pexels-roger-brown-5435847.jpg" style="width: 433px; height: 260.684px; margin: 6.60816px 0px;">


## Sumário

1. [O que é a Litecoin?](#1)
2. [Criação da Litecoin](#2)
3. [Bitcoin x Litecoin](#3)
4. [Algoritmo: Scrypt](#4)
5. [Por que Scrypt?](#5)
6. [Referência](#6)

<a id='1'></a>

# O que é a Litecoin?

A Litecoin é uma moeda digital baseada em uma rede de blockchain, de código aberto e descentralizada.

Foi uma das primeiras moedas a sair do protocolo do Bitcoin. 
Como ela é baseda no protocolo e código do Bitcoin, com apenas algumas diferenças, não apresenta whitepaper próprio.

É possível encontrar informações sobre a moeda em um vídeo de uma conferência onde o próprio criador a apresenta, que pode ser encontrado em https://www.youtube.com/watch?v=Le5ByHtssnc&t=208s&ab_channel=wedgethx

E mais informações podem ser encontradas no site oficial da moeda: https://litecoin.org/pt/

<a id='2'></a>

# Criação da Litecoin

O criador da Litecoin é o programador Charles Lee.

<img src="https://d179wquxaeob5f.cloudfront.net/wp-content/uploads/2018/08/charlie-lee-litecoin.jpg" style="width: 433px; height: 260.684px; margin: 6.60816px 0px;">

Ela foi lançada em outubro de 2021 com a justificativa de que seria uma alternativa ao Bitcoin. Uma vez que as pessoas passaram a comprar Bitcoin com a intenção de reservar a moeda por um longo prazo, a Litecoin veio com a proposta de ser uma moeda leve para ser usada em transações do dia a dia.

Tendo em vista o objetivo da moeda, Charles Lee e os contribuidores a apelidaram de "prata" para o "ouro" que era o Bitcoin.

<a id='3'></a>

# Bitcoin x Litecoin

<img src="https://static.seekingalpha.com/uploads/2017/11/29/2312271-1511971085402607_origin.png" style="width: 600px; height: 320px; margin: 6.60816px 0px;">

As principais diferenças entre o Bitcoin e o Litecoin estão no algoritmo usado e no tempo de processamento dos blocos.

Enquanto o Bircoin usa o SHA-256, para o Litecoin foi escolhido o algoritmo Scrypt como proof-of-work, por razões que veremos a seguir.

Quanto ao tempo de processamento dos blocos, a moeda é 4 vezes mais rápida para confirmar a transação, condizendo com seu objetivo de ser mais leve para transações diárias.

<a id='4'></a>

# Algoritmo: Scrypt

<img src="https://en.cryptonomist.ch/wp-content/uploads/2019/06/Proof-of-work-Scrypt-1-696x836.png">

O Algoritmo leva como parâmetro:
- Custo de CPU (**N**);
- Memória usada para cada bloco (**r**);
- Parâmetro de parametrização (**P**);
- Tamanho da saída (**dkLen**).

O input do algoritmo é a mensagem e um "sal", que passam primeiro por uma função chamada *Password-based key derivation function* que, resumidamente, faz hash da mensagem várias vezes. 
Essa função gera uma chave de tamanho 18**r** Bytes para cada bloco (e são **P** blocos).

Em seguida, cada bloco passa por uma função *ROMix* que mistura os caracteres em cada bloco.

E por fim, estes novos blocos são passados como parâmetro novamente para a função *Password-based key derivation function*, que gera uma chave do tamanho **dkLen** desejado.

<a id='5'></a>

# Por que Scrypt?

Como o SHA-256 usado pelo Bitcoin é um algoritmo mais complexo, os mineradores vêm usando métodos e equipamentos cada vez mais sofisticados para fazer a mineração, como o application-specific circuit (ASIC), e assim a atividade deixa de ser acessível.

Para dificultar estes ataques de hardware, Charles Lee programou o Scrypt ao invés do SHA-256, já que ele requer uma grande quantidade de RAM para processamento em paralelo.
Desta forma, os mineradores conseguiriam mineirar de seus CPU ou GPU. 

Na prática não ocorreu como esperado, já que o crescimento do poder das GPUs compensou a necessidade de uma grande quantidade de RAM.

<a id='6'></a>

# Referência

LITECOIN. Disponível em: https://litecoin.org/pt/. Acesso em: 26 ago. 2021.

O que é Litecoin (LTC)? A ‘Prata’ das Criptomoedas. In: THE CAPITAL Advisor. Disponível em: https://comoinvestir.thecap.com.br/o-que-e-litecoin-ltc-a-prata-das-criptomoedas/. Acesso em 26 ago. 2021.

MINING  algorithms (Proof of Work): SHA-256, Scrypt, CryptoNight, Ethash and X11. In: THE CRYPTONOMIST. Disponível em: https://en.cryptonomist.ch/2019/06/15/mining-algorithms-proof-of-work/.  Acesso em: 26 ago. 2021.

LITECOIN. In: INVESTOPIA. Disponível em: https://www.investopedia.com/articles/investing/040515/what-litecoin-and-how-does-it-work.asp. Acesso em: 26 ago. 2021.





  
  










