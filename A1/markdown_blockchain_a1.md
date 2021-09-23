# Theta Blockchain 

## Relatório A1 da disciplina de blockchain - Victor Bombarda


1. [Histórico da blockchain](#1)
2. [Características da blockchain](#2)
3. [Mecanismo de consenso](#3)
4. [Emissão da criptomoeda](#5)
5. [Interoperabilidade](#6)
6. [Referências](#4)


<a id="1"></a>
## Histórico da blockchain

Desenvolvido por Mitch Liu, desenvolvedor de jogos, e Jieyi Long, desenvolvedor da área de VR, ambos com grande contato com o mundo dos vídeo games e serviços de streaming como a Twitch. Foi inicialmente lançada em 2017 junto com o site Sliver.tv (hoje renomeada Theta.tv).

Trabalha open-source, criada para solucionar o problema de gasto com internet, armazenamento de dados e conteúdo de serviços de streaming online de vídeos, buscando terceirar esta função para os próprios usuários das plataformas.

Com o crescimento constante do tamanho dos dados devido ao avanços tecnológicos – com vídeos 4K e 8K – tem se tornado cada vez mais caro o armazenamento e o tráfego deste dados.
Assim, usuários podem compartilhar seus excessos de bandalarga e memória para manter a qualidade do streaming da plataforma e serem recompensados por este trabalho computacional.

Estes usuários que compartilham estes serviços são denominados nós cache, e são responsáveis por receber o conteúdo dos centros de distribuição de  conteúdo e 
redistribuí-lo para os espectadores da plataforma, servindo como uma ponte entre a distribuição do conteúdo e o consumidor final do conteúdo.

[White paper](https://s3.us-east-2.amazonaws.com/assets.thetatoken.org/Theta-white-paper-latest.pdf)

[Site da plataforma Theta](https://www.theta.tv/)

<a id="2"></a>
## Características da blockchain

Esta blockchain possui duas moedas:

>**Theta Token**: Governance token, usado para permitir a participação como nós validadores e/ou guardiões. Possuem também poder de voto dentro do blockchain.

>**TFUEL**: Dado como recompensa pela participação tanto como um nó guardião, sendo necessário Theta Token para participar, quanto um nó guardião, que contribui ao serviço de streaming recebendo e repassando os conteúdos.

A Theta Token é um token de governança, que não pode ser minerado tendo em vista que já foram todos previamente minerados. 
Permite que usuários tenham poder de voto na blockchain e capacidade de participar como nós validadores, como veremos mais pra frente no mecanismo de consenso.

A TFUEL é uma moeda que é veiculada na plataforma de streaming, que tem como objetivo ser usada para recompensar criadores de conteúdos e espectadores.
É minerada tanto pelos nós validadores quanto os nós de cache.

Possui um preço por transação, que custa menos do que 1 TFUEL. Tem um tempo médio de geração de bloco de 6 segundos, permitindo que transações sejam feitas e validadas de forma mais rápida.
Cada bloco tem uma capacidade de 8.192 transações, números muito maiores do que os blocos de Bitcoin, por exemplo. A blockchain possui também capacidade de mais de mil transações por segundo.

O blockchain Theta também possui a capacidade de programar smart-contracts que conforme configurados, sendo transparentes e eficazes.

Vale comentar que o "ledger" da blockchain, a sequência de bloco e os blocos em si, são passados de nós em nós devido ao fato destes se organizarem em uma rede de distribuição de dados.
Assim, estas informações chegam a cada nó participante através deste sistema de "fofoca" (como foi chamado pelos desenvolvedores), garantindo que este chegue as pontas da rede mais rápidamente, dependendo da conexão direta de todos na rede.

<a id="3"></a>
## Mecanismo de consenso

Esta blockchain usa como mecanismo o Proof-of-Stake

Como comentado acima, há dois tipos de nós (usuários participantes da blockchain):

>**Nós Validadores**: participam de conselho de outros validadores selecionados que validam e criam os blocos e tem acesso direto à cadeia completa da blockchain. Atualmente há 16 nós validadores. Para se tornar um destes hoje precisa-se mais de 10.000 Thetas “staked”.


>**Nós de Guardiões**: confirmam o trabalho feito pelos validadores, finalizando o bloco. Estes só tem acesso à cadeia completa da blockchain quando se alcançam os blocos checkpoints, blocos com “altura” múltiplo de um determinado valor inteiro. 

Assim, quando os validadores validam os dados $x$ blocos, os nós guardiões chegam juntos ao consenso do último bloco checkpoint, considerando que temos muito mais blocos guardiões do que validadores, estes dois acontecem quase que simultaneamente.

<a id="5"></a>
## Emissão da criptomoeda
Como já citado anteriormente, todas as Theta Tokens já foram mineradas, havendo no disponível 1 bilhão de tokens no mercado.
Hoje, cerca de 80% já foi liberado pelos desenvolvedores, havendo uma reserva de 20% ainda retida. Isso faz com que a moeda não possa passar por qualquer fenômeno inflacionário, porém compromete a circulação da mesma,
considerando que para participar como nós guardiões e validadores precisa-se dar 10 mil tokens em garantia, fazendo com que estes não circulem no mercado.

Para a TFUEL é diferente, não há limite para a produção desta, e esta cresce em quantidade cerca de 4% ao ano, havendo aqui um fator inflacionário nesta.
Este, porém, foi desconsiderado pelos desenvolvedores tendo em vista que com o aumento de usuários das plataformas,

<a id="6"></a>
## Interoperabilidade

Como o projeto Theta é um projeto open-source, este preve a possibilidade de interoperabilidade com outras blockchains que sejam criadas e apartir dos arcabouços básicos apresentados pelo whitepaper da mesma. 
Podendo então esta dividir e compartilhar com outras blockchains o estado de sua rede e registro de operações para garantir maior segurança da mesma.
Assim também pode-se esperar que, tendo blockchains de diferentes especialidades, blockchains que tem maior capacidade de transações por segundo podem ajudar outras blockchains a armazenar registros quando
estas não estiverem em capacidade máxima, não havendo necessidade de competição entre estas, mas cooperação.

<a id="4"></a>
## Referências

1. https://s3.us-east-2.amazonaws.com/assets.thetatoken.org/Theta-white-paper-latest.pdf

2. https://www.thetatoken.org/

3. https://www.kraken.com/pt-br/learn/what-is-theta

4. https://coinmarketcap.com/pt-br/currencies/theta/

5. https://coinmarketcap.com/pt-br/currencies/theta-fuel/
