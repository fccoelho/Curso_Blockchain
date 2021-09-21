# Pi Network
## _A primeira moeda digital que você pode minerar no seu telefone_

**Website:** https://minepi.com

**White Paper:** https://minepi.com/white-paper

**[Criadores:](https://minepi.com/team)**

- Dr. Nicolas Kokkalis, PHD em Stanford
- Dr. Chengdiao Fan, PHD em Stanford

# Sumário

1. [O que é Pi?](#1)
2. [História](#2)
3. [Principais Características](#3)
4. [Mecanismo de Consenso](#4)
5. [Função Hash e Escalabilidade das Transações](#5)
6. [Funcionamento do App](#6)
7. [Anonimidade e Privacidade](#7)
8. [Regras de Emissão](#8)
9. [Interoperabilidade](#9)
10. [Outras aplicações](#10)
11. [Junte-se ao time](#11)
12. [Elogios, Críticas e Controvérsias](#12)
13. [Conclusão](#13)
14. [Referências](#14)

<a id='1'></a>

## O que é Pi?

Em uma era de grande valorização dos criptoativos, cuja maioria das criptomoedas são muito difíceis de serem transacionadas e, principalmente, mineradas por pessoas comuns, surge a Pi: uma criptomoeda feita por e para pessoas comuns. Qualquer um com um celular e o aplicativo instalado, pode facilmente minerar  Pi, ou seja, dispnibilizar a sua máquina para processar transações, ajudar a proteger, aumentar a confiabilidade da rede e receber uma certa quantidade Pi como recompensa. A criptomoeda Pi ainda não possui um valor monetário, mas isso não a configura como uma fraude. Pelo contrário, Pi é um projeto extremamente genuíno, criado por uma equipe de pós-graduados da Universidade de Stanford, que possui o intuito de revolucionar a relação das pessoas com as criptomoedas e conta com uma comunidade que vem crescendo a cada dia. É um projeto pensado para o longo prazo, cuja construção é coletiva, o sucesso ainda não está garantido e depende de uma grande dedicação da equipe fundadora. Dentre os principais desafios da Pi, se encontram estabelecer uma infraestrutura da rede, desenvolver tecnologias, distribuir a criptomoeda e assim, construir uma comunidade engajada pelo projeto.

**Missão:** Construir uma plataforma de criptomoeda e contratos inteligentes protegida e operada por pessoas comuns.

**Visão:** Construir o mercado de ponto a ponto (P2P) mais inclusivo do mundo, alimentado por Pi, a criptomoeda mais usada do mundo.

<a id='2'></a>

## História

Pi foi idealizada como um projeto de 3 fases:

1. **Fase 1 (Planejamento, Distribuição, Bootstrap do Gráfico de Confiança):** Possui o objetivo de aumentar o número de usuários na rede e melhorar a experiência e o comportamento do usuário. Já é possível minerar por um emulador de Pi, mas não é possível transacionar Pi, pois durante essa fase, a criptomoeda ainda não está listada em Exchanges.
2. **Fase 2 (Rede de Teste):** A implantação do software em uma Rede de Teste usará o mesmo gráfico de confiança da rede principal, mas em uma moeda Pi de teste. A equipe principal hospedará nessa rede varios nós de teste, juntamente com os nós que os usuários criarem. A rede então será executada em paralelo com o emulador Pi da fase 1 e, periodicamente, os resultados serão comparados e utilizados para implementar mudanças e consertar bugs. Essa execução simultânea será feita até a rede de teste alcanças resultados consistentes ao do emulador.
3. **Fase 3 (Rede Principal):** Quando a comunidade sentir que o software está pronto, a rede principal Pi será lançada. A rede de teste e o emulador serão desligados, as moedas dos usuários migrarão para rede principal e o sistema continuará por conta própria para sempre. Atualizações futuras serão fornecidas pela comunidade de desenvolvedores e pela equipe principal, e a implementação dependerá de nós que atualizam o software de mineração (igual outros blockchains). Nenhuma autoridade controlará a moeda e ela será totalmente descentralizada. Saldos de usuários falsos ou duplicados serão descartados.


A Fase 1 do projeto foi lançada em 14/03/2019, e atualmente está na Fase 2, apesar de não ter informação no site de quando ela começou. Também está acontecendo nesse mês de setembro a última fase de um hackathon que começou em 28/06/2021. Nesse [Pi Hackathon](https://minepi.com/hackathon), usuários se unem em grupos para participar em duas categorias:

- Aplicativos de Ecossistema: aplicativos que melhoram o ecossistema e as funções do Pi;
- Aplicativos de Negócios: aplicativos que atendem a um produto comercial ou de consumo;

Com prêmios que somam 100 mil dólares e 100 mil Pi, o objetivo é a união dos usuários para a construção do futuro de Pi juntos. Nessa última fase, a comunidade está votando para decidir os vencedores do Hackathon.

<a id='3'></a>

## Principais Características

Segundo o próprio site, as principais características de Pi são:

- **Principal diferencial:** A primeira moeda digital que você pode minerar no seu celular;
- Mineração simples, com uma interface intuitiva e transparente, quebrando as barreiras que impedem pessoas comuns de minerarem;
- Distribuição justa, dando a uma grande massa da população mundial acesso à Pi;
- Ganhos meritocráticos, pois recompensa as contribuições de cada usuário para construir e manter a rede;
- Equilíbrio, entre a criação de uma sensação de escassez de Pi e a garantia de que não haverá uma grande acumulação de Pi pra um número muito pequeno de pessoas;
- Não agressão ao meio ambiente, devido ao baixo consumo energético pelo processo de mineração.

<a id='4'></a>

## Mecanismo de Consenso

O Mecanismo de consenso de Pi é baseado no Stellar Consensus Protocol (SCP) e no Federated Byzantine Agreement (FBA).
Visando ordenar uma lista de blocos de transações, esses algoritmos funcionam sem desperdício de energia, mas exigem a troca de muitas mensagens, pois somente após várias rodadas de votação dentro de grupos de confiança da rede de computadores, é possível chegar a um acordo sobre quais transações registrar em um bloco e a ordem desses blocos. Funciona semelhantemente à seguinte forma: "Eu voto no bloco A para ser o próximo bloco. E confirmo que a maioria dos nós em que confio também votou no bloco A", após várias afirmações dessa, é possível concluir que A é o próximo bloco. Mesmo que essas etapas pareçam ser uma quantidade grande, a internet é rápida e as mensagens são leves, portanto esses algoritmos de consenso são mais leves do que outros, como a prova de trabalho da Bitcoin, por exemplo.

Um dos principais representantes desses algoritmos é o Byzantine Fault Tolerance (BFT), porém um dos seus problemas é a determinação centralizada (principalmente pelo criador do sistema) do quorum de votação. Já no FBA, cada nó define suas próprias "fatias de quorum", permitindo que os nós possam ingressar na rede de forma descentralizada: eles declaram os nós de confiança e convencem outros nós a confiar neles, sem necessidade de convencer alguma autoridade central. E o SCP, é uma instanciação do FBA, em que temos os quoruns sendo formados com base nas fatias de quorum de seus membros, e um validador só aceitará novas transações se, e somente se, uma determinada proporção de nós em seus quoruns também aceitarem a transação.

Diferentemente do SCP que possui principalmente empresas e instituições como nós, o algoritmo de consenso de Pi pretende permitir que dispositivos de indíviduos contribuam e sejam recompensados (por exemplo: celulares, notebooks ou computadores). Além disso, Pi divide em quatro as funções que os usuários podem desempenhar:

1. **Pioneiro:** Um usuário do app que só valida sua presença diariamente, confirmando que não é um robô;
2. **Contribuidor:** Um usuário que contribui com uma lista de pioneiros que conhece e em que confia, contribuindo para a construção da rede de confiança global;
3. **Embaixador:** Um usuário que introduz outros usuários na rede Pi;
4. **Nó:** : Um usuário que executa o software Pi Node em seu computador. Esse software executa o algoritmo SCP modificado, levando em consideração as informações da rede de confiança fornecida pelos contribuidores.

Um usuário pode desempenhar mais de uma dessas funções, e todas elas são consideradas como mineração, por isso, possuem recompensas diárias de Pi recém-minerado. Como, até o momento, o software Pi Node ainda não foi lançado, só é possível exercer as três primeiras funções.

<a id='5'></a>

## Função Hash e Escalabilidade das Transações

Como o software Pi Node ainda não foi lançado, não é possível saber a função hash utilizada, mas sabe-se que na fase 3 do projeto, cada usuário terá suas próprias chaves privadas/públicas. Quanto à escalabilidade de Pi, deve ser semelhante ao Stellar, que por sua vez suporta milhares de transações por segundo. Como o software será código aberto, a partir do seu  momento do lançamento, essas dúvidas serão sanadas.

<a id='6'></a>

## Funcionamento do App

**[Imagem 1](https://imgur.com/a/y42RzUj)**

- **Imagem 1:** Para criar uma conta no aplicativo, existem duas opções: login com o Facebook, ou login com o número de telefone. Em seguida, você deve informar seu nome completo, um nick (única informação que os outros usuários terão acesso) e já está criada a conta;
- **Imagem 2:** É possível encontrar facilmente um menu com várias opções dentro do aplicativo, desde o seu perfil pessoal e círculo de confiança, até o white paper da criptmoeda;
- **Imagem 3:** Interface intuitiva do aplicativo, onde mostra a quantidade de Pi que você tem, a taxa que você está minerando, dentre outras informações;
- **Imagem 4:** Perguntas Frequentes, e chats para tirar dúvidas e conhecer outros usuários de Pi.

Além disso, vale ressaltar que o aplicativo não afeta o desempenho do telefone, não consome bateria e nem dados de internet. Além disso não é preciso deixar o app aberto para a mineração acontecer, basta clicar no botão com um símbolo de relâmpago e fechar o aplicativo. Supondo que serão gastos apenas 20 segundos por dia nesse processo, ao final de um ano serão gastos um total de apenas 2 horas, para minerar Pi durante 365 dias.

<a id='7'></a>

## Anonimidade e Privacidade

Como citado no tópico anterior, os demais usuários da rede só têm acesso ao seu nick, permitindo assim a total anonimidade. Quanto aos dados pessoais que o aplicativo tem acesso, eles não são expostos ou compartilhados com nenhuma outra empresa ou pessoa, assegurando a privacidade. Todavia, caso o login seja feito com o Facebook, a rede social saberá que você tem uma conta no Pi network. Além disso, devido ao recurso de rede de confiança, não há sistema computacional no mundo que possa alterar um bloco ou retirar informações privadas acerca das transações dentro da blockchain. Além disso, quanto mais nós a rede Pi tiver, mais seguro ela será tanto em relação a anonimidade, quanto em relação à privacidade.

<a id='8'></a>

## Regras de Emissão

O fornecimento de criptomoeda por hora é definido pela função: T = P + C + E, e o significado de cada um desses termos está a seguir:

- P = Recompensa por ser pioneiro, calculada por P = integral(f(n) dx), onde f é uma função declinante logaritmicamente e n o número de usuário. Atualmente, a taxa básica de mineração diminui pela metade sempre que o número de usuários ativos aumenta em um fator de 10 (por exemplo, indo de 1 milhão para 10 milhões). Essa taxa acabará caindo para 0 quando a rede atingir um certo número de usuários, e a partir desse ponto, os novos mineradores passarão a ser recompensados por meio de taxas de transação e não pela cunhagem de novas moedas. Além disso, é válido ressaltar que pra cada usuário, existe um limite (igual pra todos) de quantidade de Pi pré-cunhada a qual ele terá acesso ao longo da vida de membro;
- C = Recompensa por conexões de confiança, calculada por C = r x P, onde r é uma taxa de conexões, sendo 20% pra cada conexão. Cada pessoa pode ter até 5 pessoas no seu círculo de confiança.
- E = Recompensa por embaixador, calculada por E = t x (P+C), onde t é uma taxa de ganhos de novos membros, sendo 25% pra cada membro ativo que você ganhou pro aplicativo, e também 25% se o membro que convidou você continua ativo.

Um exemplo: Eu entrei na época que a taxa estava P = 0.1 pi/h, tenho uma pessoa no meu círculo de confiança, então C = 0.2 x 0.1 = 0.02 pi/h e a pessoa que me convidou continua ativa, então E = 0.25 x (0.12) = 0.03 pi/h. Totalizando em T = 1.5 pi/h.

<a id='9'></a>

## Interoperabilidade

A única interoperabilidade atual vem da semelhança existente com o mecanismo de consenso SCP da Stellar, que pode vir a permitir alguma interoperabilidade entre essas duas criptomoedas.

<a id='10'></a>

## Outras aplicações

No momento ainda não existem outras aplicações, mas esse é um dos objetivos da equipe fundadora. A comunidade Pi espera que os usuários possam contribuir com isso, de tal forma que o aplicativo móvel também servirá como um ponto de vendas onde os membros de Pi podem oferecer seus produtos e serviços por meio de uma "vitrine virtual" para outros membros da rede, e toda transação de compra e venda será feita utilizando a moeda Pi.

Além disso, também objetiva-se permitir que desenvolvedores de aplicativos possam utilizar a infraestrutura existente de Pi, juntamente com os recursos compartilhados da comunidade e dos usuários, para realizar o seu trabalho sem ter que começar do zero. Tudo isso, com um grau de interoperabilidade entre o aplicativo Pi Network e os outros aplicativos.

<a id='11'></a>

## Junte-se ao time

Ao clicar no botão **["Junte-se ao time"](https://docs.google.com/forms/d/e/1FAIpQLSemnCpPezFCCJmu9S7LSH_2SsqccutQ0HjV8dixJcVTQthKJw/viewform)** na aba [Equipe](https://minepi.com/team) no site oficial do Pi Network, você será imediatamente direcionado a um Google Forms com a seguinte mensagem: "Estamos atualmente à procura de alunos talentosos para nos ajudar nas áreas de Sistemas Distribuídos, Desenvolvimento de Back End e Front End, Cientistas Sociais e Empresários". E rapidamente você pode mandar sua inscrição para algum trabalho remunerado no desenvolvimento de Pi.

<a id='12'></a>

## Elogios, Críticas e Controvérsias

Desde 2019, saíram diversas notícias sobre a criptomoeda, havendo desde elogios e previsões de Pi ser a próxima super criptmoeda, até acusações de fraudes e de envolvimento em vazamento de dados. A seguir está os links para algumas dessas notícias:

- [Pi Network - a próxima super criptomoeda](https://www.dinheirolimpo.com/post/pi-network-a-pr%C3%B3xima-super-criptomoeda) - O  autor explica brevemente sobre a criptomoeda, além de comentar como ela pode ter um futuro promissor;
- [Pi Network: Qual é a última previsão para a moeda Pi?](https://capital.com/pi-network-pi-coin-price-prediction-2021-2025) - A autora comenta algumas projeções de valores de Pi para os próximos 5 anos., projetando, inclusive, que no momento do lançamento de Pi, é provável que seu valor seja por volta de $1;
- [Criptomoeda Pi Network usa tática de esquema de pirâmide financeira para atrair usuários](https://portaldobitcoin.uol.com.br/criptomoeda-pi-network-usa-tatica-de-esquema-de-piramide-financeira-para-atrair-usuarios/) - A principal reclamação do autor é o fato da criptomoeda utilizar certas táticas duvidosas, as quais ele compara com táticas usadas por companhias de marketing multinível e pirâmides financeiras;
- [Aplicativo móvel de 'mineração' de criptomoedas está possivelmente conectado ao vazamento de dados pessoais](https://cointelegraph.com.br/news/mobile-crypto-mining-app-possibly-connected-to-personal-data-leak) - O autor comenta sobre um caso de vazamento de dados, supostamente conectado ao aplicativo Pi Network, no Vietnã.

<a id='13'></a>

## Conclusão

Atualmente a criptomoeda Pi ainda não é relevante, mas após atingir a Fase 3, tem um grande potencial de crescimento, podendo vir a se tornar a próxima super criptomoeda. Devido a comunidade ativa e ao grande esforço da sua equipe nesse projeto, não me resta dúvidas que ainda ouviremos falar muito bem dela no futuro. O grande diferencial de Pi é ser uma moeda digital que pode ser minerada no telefone, algo realmente incrível e altamente inclusivo com as pessoas em geral.

<a id='14'></a>

## Referências

- https://minepi.com/
- https://minepi.com/hackathon
- https://imgur.com/a/y42RzUj
- https://docs.google.com/forms/d/e/1FAIpQLSemnCpPezFCCJmu9S7LSH_2SsqccutQ0HjV8dixJcVTQthKJw/viewform
- https://www.dinheirolimpo.com/post/pi-network-a-pr%C3%B3xima-super-criptomoeda
- https://capital.com/pi-network-pi-coin-price-prediction-2021-2025
- https://portaldobitcoin.uol.com.br/criptomoeda-pi-network-usa-tatica-de-esquema-de-piramide-financeira-para-atrair-usuarios/
- https://cointelegraph.com.br/news/mobile-crypto-mining-app-possibly-connected-to-personal-data-leak
