# Cardano (ADA)  

## Histórico 

A Cardano é uma blockchain de terceira geração. Sua história inicia em 2015, quando foram iniciadas as pesquisas e o desenvolvimento de um projeto para a criação de uma criptomoeda escalável e sustentável; dois anos depois, em 2017, ela foi lançada, ensejando a circulação de *ada*, como foi chamada, em homenagem à [Ada Lovelace](https://pt.wikipedia.org/wiki/Ada_Lovelace), sua criptomoeda. Aliás, a Cardano, em oposição a outras blockchains populares, não tem um white paper [1]; o mecanismo de consenso utilizado por ela, baseado em uma prova de participação (*proof-of-stake*) nomeada *Ouroboros* [2], será brevemente descrito nas seções seguintes. 

Além disso, o projeto é dividido em cinco etapas, que, como o seu mecanismo de consenso, são peculiarmente nomeadas em homenagem a escritores: [Byron](https://pt.wikipedia.org/wiki/Lord_Byron), caracterizada pela fundação e distribuição da plataforma, [Shelley](https://pt.wikipedia.org/wiki/Mary_Shelley), que visou ao recrudescimento da descentralização, [Goguen](https://en.wikipedia.org/wiki/Joseph_Goguen), que, recentemente, ensejou a introdução de *smart contracts*,  [Basho](https://en.wikipedia.org/wiki/Matsuo_Bash%C5%8D), que viabilizará a otimização alicerçada na introdução de *sidechains* (que servirão 1) como um mecanismo de *sharding*, ou "fragmentação", e 2) como ambientes seguros para verificação de novas features),  e [Voltaire](https://pt.wikipedia.org/wiki/Voltaire), que, auspiciosamente, relegará a administração da rede totalmente aos participantes, os *stakeholders* (o desenvolvimento, no momento, é estimulado pela IOHK [3]): por um lado, novas features serão propostas e votadas; por outro lado, parte das taxas de transação será armazenada para sustentar o desenvolvimento destas features escolhidas pelos stakeholders. Atualmente, a equipe da IOHK está trabalhando para o desenvolvimento desta blockchain; as informações estão disponíveis neste bonito [roadmap](https://roadmap.cardano.org/en/goguen/). 


## Descrição da blockchain 

O principal aspecto da Cardano é a utilização de um mecanismo de consenso alicerçado na prova por participação; sua segurança, além disso, é matematicamente assegurada, e os *papers*, como os códigos, que, peer-reviewed, garantem esta segurança estão disponíveis para o público. Isso é importante porque, conforme está escrito em [2], mecanismos de consenso sustentados na prova de trabalho (por exemplo, o Bitcoin) exigem, imperativamente, um consumo enérgetico gigantesco; em 2017, por exemplo, quando [2] foi escrito, a manutenção da cadeia do Bitcoin exigia a produção energética de um país enxuto. Contrastivamente, a Cardano sugere que sua cadeia exige o consumo energético de uma casa enxuta [4, 5]. A seção seguinte, nesse sentido, proporciona uma breve descrição do mecanismo de consenso utilizado pela Cardano; informações mais detalhadas estão disponíveis em [2].

### Ouroboros 

Ouroboros é, como escrevemos, um protocolo alicerçado na prova de participação. A inserção de novos blocos, nesse sentido, é, em oposição ao mecanismo de prova de trabalho, em que o indivíduo que inserirá o bloco, o "minerador", é escolhido a partir de seu poder computacional, feita por um participantes (em maior detalhe, um grupo de participante; o parágrafo seguinte explorará isso) escolhido de maneira randomizada; e a probabilidade de ele ser escolhido é proporcional à sua participação, ao seu *stake*, na blockchain [2]; na Cardano, em particular, esta quantidade é mensurada a partir do patrimônio, em ada, do usuário. 

Explicitamente, o Ouroboros divide a cadeia em *epochs* que, então, são divididos em *time slots*; estes, neste contexto, gozam de um líder, que são equivalentes, na cadeia do Bitcoin, aos mineradores. Estes líderes, por sua vez, precisam garantir a alimentação da cadeia; para isso, é importante garantir que os usuários estejam online em toda extensão do tempo. Nesse sentido, os líderes podem *delegar* a responsabilidade de executar o protocolo, procedimento que incrementará a cadeia; esse processo, naturalmente, culmina na formação de *stake pools* [2], que funcionam como as [mining pools](https://en.wikipedia.org/wiki/Mining_pool) do Bitcoin. As recompensas, nesse caso, são distribuídas entre os participantes desta stake pool e são proporcionais à quantidade de ada usufruída pelos usuários; elas são, aliás, advindas de uma de duas fontes: reserva ou taxas de transação. 

No entanto, o Ouroboros precisa garantir a segurança da cadeia: por exemplo, como os indivíduos são escolhidos com base em seu patrimônio, temos, para evitar centralização, que desincentivar o acúmulo de moedas. Para isso, a proporcionalidade da recompensa pela inserção do novo bloco é limitada; precisamente, é definido um threshold `x` que, se violado, estabelece a constância das recompensas; um indivíduo com `x + epsilon` do total de ada em circulação na cadeia, desse modo, será recompensado da mesma forma que um indivíduo com `x` do total de ada para qualquer `epsilon` positivo. Em particular, os participantes são desincentivados a possuir mais de `x` do patrimônio disponível. 

Além disso, temos, nesse protocolo, a garantia de que, se `50 + epsilon` por cento dos usuários são honestos, a cadeia é inócua a ataques por participantes adversários [2, 5]. Contudo, não exploraremos, neste excerto, este tópico em mais detalhes.  



[1](https://en.wikipedia.org/wiki/Cardano_(blockchain_platform)) Cardano (blockchain platoform), Wikipedia. Acessado em 20 de setembro de 2021. 

[2](https://eprint.iacr.org/2016/889.pdf) Aggelos Kiayias and Alexander Russell and Bernardo David and Roman Oliynykov. (2016). Ouroboros: A Provably Secure Proof-of-Stake Blockchain Protocol.   

[3](https://github.com/input-output-hk) Input Output, IOHK. GitHub. Acessado em 20 de setembro de 2021. 

[4](https://roadmap.cardano.org/en/shelley/) Cardano Roadmap: Shelley. Acessado em 20 de setembro de 2021. 

[5](https://iohk.io/en/blog/posts/2020/03/23/from-classic-to-hydra-the-implementations-of-ouroboros-explained/) From Classic To Hydra: the implementations of Ouroboros explained. Acessado em 20 de setembro de 2021. 
