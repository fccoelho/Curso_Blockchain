# Ripple (XRP)
## Emanuel Bissiatti de Almeida <br/> 


Ripple não é uma criptomeda, é sim uma empresa que atualmente oferece um sistema global de pagamentos que possui uma criptomoeda - a XRP - no centro deste sistema. Barato e eficiente, a empresa propoem o seu sistema para as instituições financeiras como uma modernização do sistema bancário global. </br>

### História

A antecessora da Ripple foi criada pelo desenvolvedor Web Ryan Fugger em 2004. Na época o desenvolvedor criou a Ripplepay com o objetivo de oferecer um sistema de pagamentos distribuido de baixo custo. Infelizmente, o produto não obteve muito sucesso. </br>

Já com a chegada do Bitcoin, houve uma revolução no mundo financeiro tecnológico, porém ele obteve algumas críticas como o auto custo energético necessário para suportar a rede e a lentidão para aprovar as transações. Dessa forma, no ano de 2011 um programador chamado Jed McCaleb desenvolveu um tecnologia de consenso distribuido mais eficiente e barata que a rede bitcoin. Assim, aliado de Chris Larson, David Schwartz, Arthur Birtto, e Jed McCaleb, Ryan Fugger evoluiu o seu sistema de pagamentos, no ano de 2012, com o protocolo Ripple Transaction Protocol (RTXP). Esse protocolo permitia a transação de diversas moedas incluindo o Euro, o Dólar e o Bitcoin, mas a grande estrela deste sistema é o XRP. O XRP é uma criptomoeda não minerável criada pela empresa para o funcionamento desse sistema com alta escalabilidade e um baixo custo. </br>

No ano de 2014, Ripple focou-se em oferecer suporte as instituições financeiras. Propondo ser uma alternativa ao sistema bancário que precisa de atravessadores para realizar uma transação internacional: "Ripple simplifica o processo de troca, criando transferências ponto a ponto e transparentes nas quais os bancos não precisam pagar taxas bancárias correspondentes." Assim, no ano início daquele ano o banco alemão Fidor Bank foi o primeiro a anunciar uma parceria com a Ripple, adotando o seu sistema. Por discordancias com o rumo tomado pela empresa,  Jed McCaleb, abandonou a equipe para desenvolver a sua própria moeda: stellar. </br>

Nos anos seguintes, diversas instituições financeiras aderiram ao sistema da Ripple como o Santander, o HSBC e o Bank of America. Porém, algumas pessoas ainda possuem algumas críticas ao sistema, a maior delas é a centralização e influência sobre o sistema. Por não haver mineração, todas as moedas XRP já foram criadas em 2012 e cerca de 40% delas estão sobre domínio da empresa. Além disso, o sistema de pagamentos, apesar de descentralizado, está sobre controle da Ripple e das instituições financeiras, já que não há mineração, não existe incentivos financeiros para tal. </br> 
 
### A moeda XRP

Pensando num sistema de baixo custo para pagamentos, a moeda XRP foi emitida completamente em 2012: 100 Bilhões de moedas, sem a necessidade de mineração. Sendo que 60% das moedas estão sobre domínio da empresa. A principal função da moeda é para pagar as taxas das transações sobre a Ripplenet, ainda que baixas comparadas as outras criptomoedas, para garantir as segurança e evitar spam de transações e contas falsas. Além disso, a XRP pode ser utilizada como moeda de troca quando não há a quantidade de moedas requisitadas pelos clientes em circulação na rede, semelhante ao dólar que é utilizado nas transações internacionais. 


### Como funciona

A Ripple oferece um sistema de pagamentos global, e não uma criptomoeda. De maneira descentralizada, a Ripple e instituições financeiras parceiras possuem o controle da Ripplenet, a rede de pagamentos da empresa. De acordo com o Whitepaper da Ripple, a rede para se manter segura precisa resolver o problema do consenso Bizantino. Nesse problema, o general que está liderando uma invasão a uma cidade precisa decidir junto com os seus comandantes se o exército deve invadir a cidade. O problema é que os comandantes estão espalhados ao redor da cidade e não se sabe há ou não mensageiros e comandantes traidores. Analogamente, um rede de criptomoedas precisa garantir se uma transação ocorreu sem fraudes. Em uma rede todos os agentes precisam obter o conhecimento da transação para não haver duplicação de moedas, se alguém realizou uma transação a rede precisa contabilizar. 

Com o objetivo de resolver esse problema, a Ripple usa o protocolo Ripple Transaction Protocol (RTXP) que usa o algoritmo de votos para validar as transações que só são concluidas quando 80% da rede aceita a transação. 
Esse protocolo funciona de acordo com alguns atores:

* O server: estrutura que executa os software da Ripple, similar aos servidores web.

- Ledger: é o livro onde se armazena o valor contido em cada carteira. 

* Last-Closed Ledger: representa o último livro avaliado por consenso, representa o estado atual da rede

- Open Ledger: o livro de cada nó que armazena as informações de transações realizadas por ele mas que ainda não foram aprovadas em consenso

* Unique Node List (UNL): lista de nós que vão validar a operação.

- Proposer: Ato de propor um transação

Dado esse atores, o sistema funciona da seguinte forma:

* Antes de iniciar as rodadas de consenso, cada servidor obtém todas as transações válidas que ainda não foram concluidas e as mantém públicas no “candidate set” (Conjunto de candidatos)

- Em seguida, cada servidor mistura os “candidate set” de sua UNL e então vota na veracidade das transações 

* Se a quantidade de votos "sim" de uma transação for suficiente, a transação passa uma próxima rodada. Caso contrário, a transação será abortada ou será inclusa no próximo processo de consenso. 

- Por fim, a última rodada de consenso consiste em uma aprovação de no mínimo 80% porcento da rede UNL de um servidor. Se aprovada, as transações são adicionadas a livor-razão (Last-Closed Ledger) e este é atualizado. 

Segundo o Whitepaper, a segurança da rede é garantida pela quantidade de votos necessário para aprovar uma transação. Da rede, 80% precisa aprovar a rodada de votos e são realizadas várias rodadas para aumentar a segurança, de modo que a probabilidade de um nó corrompido danificar uma rede com muitos nós é baixa. 

Diferente de outras redes de criptomoedas, a Ripplenet usando o seu sistema de votos, permite a transação de moedas fundiárias e outras criptomoedas. Com o auxílio de instituições financeiras a empresa obtém a liquidez das outras moedas não-XRP e confiança do cliente final que pode estar utilizando indiretamente os serviços da Ripple. 


### Conclusão 

Assim, a Ripple permite um sistema de pagamentos rápido, eficiente, escalável e de baixo custo. Isso é possível graças ao algoritmo de aprovação por votos e a controle da rede por parte de servidores da empresa, não necessitando de mineradores descentralizados para garantir as transações. Com isso, segundo informações oficiais, a RippleNet concluiu as transações em até 4 segundos e pode realizar até 1500 transações por segundo (apesar de não operar em sua capacidade máxima). Aliando-se a parte do sistema financeiro, como o banco Santander, a Ripple entrega um sistema de pagamentos sólido com potencial de crescer. Porém, não está livre de críticas, a empresa possuiu grande influência sobre a rede e a sua moeda. De qualquer forma, é importante acompanhar o projeto, só o tempo dirá se esta moeda irá vingar no atual mundo concorrido das criptomoedas. 


### Bibliografia:

* [Whitepaper](https://ripple.com/files/ripple_consensus_whitepaper.pdf)

* [Site oficial](https://ripple.com/)

* [Wikpidia](https://pt.wikipedia.org/wiki/Protocolo_de_Pagamento_Ripple)

