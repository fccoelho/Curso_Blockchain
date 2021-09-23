# Sumário

1.  [O que é Audius](#org24b91b3)
2.  [Histórico](#orgb51ea99)
3.  [Principais features](#org571b54e)
4.  [Mecanismo de consenso](#org588e4a4)
5.  [Função Hash](#orga632e57)
6.  [Anonimidade](#org3e33662)
8.  [Emissão](#orgc7fee82)
9.  [Interoperabilidade](#orgd30bf4f)
10. [Casos de uso](#orgbc070d2)
11. [Referências](#orgdb7acc4)



<a id="org24b91b3"></a>

# O que é Audius

Audius se autodenomina um protocolo musical do futuro, é um protocolo de compartilhamento e streaming de música descentralizado que facilita as transações diretas entre ouvintes e criadores, dando a todos a liberdade de distribuir, monetizar e transmitir qualquer conteúdo de áudio. 
O sistema de distribuição de música no mundo tem muitos intermediários nebulos desde sua criação, a mecânica de distribuição dos valores e acumulação dessas propriedades intelectuais ainda é por grande parte muito ofuscada e poluída, hoje com a tecnologia esses médios não são mais necessários e podem ser substituídos por essa Blockchain que conecta músicos e ouvintes de uma forma muito mais direta e clara. Tradicionalmente, as gravadoras e outros intermediários da indústria musical ficam com a maior parte de todas as músicas ou álbuns vendidos. De acordo com algumas estimativas, apenas cerca de 12% das receitas da indústria da música foram pagas aos artistas. Audius pretende se destacar de seus concorrentes, direcionando 90% da receita musical para artistas. 
O Discord para dúvidas e acompanhamento da comunidade existe e é ativo de acordo com atualizações e notícias que vem e vão. Além do Twitter que é rápido e preciso com as informações relacionadas a Blockchain.
[Discord da comunidade Audius](https://discord.com/invite/audius)
[Twitter da Audius](https://twitter.com/AudiusProject)
O repositório de protocolo Audius é um mono-repositório que contém todas as peças que fazem e dão suporte ao protocolo, incluindo contratos inteligentes, serviços e outras bibliotecas de suporte.
[Repositório de Protocolo](https://github.com/AudiusProject/audius-protocol)
A moeda utilizada se chama Áudio e com esse mesmo nome utilizado nas principais plataformas de negociação de criptomoedas. No projeto da Audius há cerca de 406 milhões de moedas Áudio em circulação e com um fornecimento total de cerca de 1 bilhão, com uma capitalização de mercado de cerca de 5 bilhões de reias, o índice de classificação fora do mercado é de 97° lugar, sua fama e destaque começou a aperecer em 2020.
[White Paper da Audius](https://docs.audius.org/welcome)


<a id="orgb51ea99"></a>

# Histórico

O desenvolver da plataforma Audius começou em 2018 e arrecadou cerca de 5,5 milhões de dólares em agosto daquele ano, após completar uma rodada da Série A que incluiu General Catalyst, Lightspeed e Pantera Capital.
O protocolo Audius teve seu início no segundo semestre de 2020 com o objetivo de simplificar e competir com serviços de streaming de música, simplificando e gerando uma nova estrutura sem burocráticos contratos fixos de gravações musicais assim como é feito em grandes gravadoras atualmente, mais precisamente a rede principal da Audius foi lançada em 24 de setembro de 2019, porém o whitepaper foi lançado apenas em outubro de 2020, e já tem cerca de 6 milhões de usuários porém pode parecer quase imperceptível dados que o Audius representa cerca de 2% dos estimados 445 milhões de assinantes de straming de música em todo o mundo. Recentemente fechou uma parceiria com o popular e famoso TikTok, porém o conhecimento do público geral veio antes com uma matéria na revista Rolling Stone.
[Notícia do Canaltech sobre a parceiria Audius e TikTok](https://canaltech.com.br/redes-sociais/tiktok-fecha-parceria-para-facilitar-envio-de-musicas-na-plataforma-192827/)
A Audius nasceu no Blockchain da Ethereum e muito provável que bem na época que foi criada houve grandes altas de preço e isso inviabilizou a utilidade da rede, logo em seguida houve uma mudança para a Blockchain da Solana (competidora do Ethereum que ganhou notoriedade pela capacidade de entrega de seus protocolos), se trata de uma rede muito mais rápida que já está implementada e supera e muito as transações por segunda da Ethereum, sendo assim uma ótima mudança para a Audius. Esse processo de transição ainda está em andamento.
[Explicação do que é Solana e por que é a Blockchain mais poderosa do momento](https://forkast.news/what-is-solana-why-hottest-blockchain/)

Esse protocolo foi escrito por 4 pessoas principais: 
* Ronell Rumburg (Co-Fundador e Chefe Executivo)
  * Se envolveu na empresa no Seed Investment, antes do desenvolvimento do produto
  * Co-Fundador da BackSlash, que se trata de uma carteira de criptomoeda online simplificada que é compatível com dispositivos móveis e pode ser vinculada com qualquer uma de suas identidades virtuais, como endereço de e-mail, Facebook ou Twitter.
* Forrest Browning (Co-Fundador e Chefe de Produtos)
  * Apareceu na Forbes Under 30
  * Co-Fundador da StacksWare, uma empresa de gestão de dados gerada por um projeto de Stanford em 2017.
* Sid Sethi (Senior Engineer)
  * Bacharelado em Engenharia da Computação na Carnegie Mellon University
  * Já trabalhou em grandes empresas como na Venture Capital Anlyst, eBay e The Blackstone Group como Analista e Engenheiro de Software.
* Hareesh Nagaraj (Staff Enginner)
  * Bacharelado em Ciência da Computação no The College of Willian and Mary
  * Trabalhou como Engenheiro de Software II no Microsoft Azure Service Fabric Team

<a id="org571b54e"></a>

# Principais Features

Sendo Audius um protocolo de compartilhamento de música descetralizado, de propriedade da comunidade e controlado pelo artista, temos uma alternativa baseada em Blockchain para para plataformas de streaming existentes para ajudar os artistas a publicar e monetizar suas propriedades intelectuais e ditribuí-las diretamente ao público.
O Audius tem três tipos de usuários:
* **Artistas:** Carregam suas Faixas, Álbuns, Competições, Imagens, num geral todo o conteúdo necessário e compartilham com os seguidores
* **Fãs:** Escutam as devidas produções musicais e podem criar suas playlists, se inscrevem e seguem quem quiser
* **Provedores de Serviço:** Sustentam o tráfego de aplicativos, protegem e garantem a segurança da rede e podem acessar conteúdos também
   * Provedores de seriço podém prover um ou mais dos seguintes serviçis via staking de Audio:
   * Nó de descoberta: (hospedar um endpoint com suporte SSL e registrar o endpoint com stake)
   * Nó de conteúdo: (hospedar um endpoint com suporte SSL e registrar o endpoint com stake)
  
Para descrever as características da Blockchain é necessário explicar seus Nós (Nodes), seus Smart Contracts e Libs. Assim sendo temos:

**Audius Services**

Serviço | Descrição
------------ | -------------
[Nó de Conteúdo](https://github.com/AudiusProject/audius-protocol/tree/master/creator-node) | Mantém a disponibilidade do conteúdo dos usuários no IPFS, incluindo metadados do usuário, imagens e conteúdo de áudio
[Nó de descoberta](https://github.com/AudiusProject/audius-protocol/tree/master/discovery-provider) | Indexa e armazena o conteúdo dos contratos Audius no blockchain para clientes consultarem por meio de uma API
[Serviço de Identidade](https://github.com/AudiusProject/audius-protocol/tree/master/identity-service) | Armazena textos criptografados de autenticação, faz OAuth do Twitter e transmite transações em nome dos usuários

Audius Smart Contracts e Libs

Lib | Descrição
------------ | -------------
[Libs](https://github.com/AudiusProject/audius-protocol/tree/master/libs) | Uma interface fácil para a web distribuída e serviços Audius: Serviço de Identidade, Discovery Node (provedor de descoberta) , Content Node (criador)
[Contratos](https://github.com/AudiusProject/audius-protocol/tree/master/contracts) | Os contratos inteligentes sendo desenvolvidos para o protocolo de streaming Audius
[ETH-contracts](https://github.com/AudiusProject/audius-protocol/tree/master/eth-contracts) | Os contratos inteligentes Ethereum sendo desenvolvidos para o protocolo de streaming Audius

**Segurança**

Vale ressaltar que toda faixa de áudio criada na plataforma é feita como TimeStamp e isso permite que seja possível fazer o tracking e verificar qualquer tipo de pirataria, podendo assim impedir isso de acontecer. Assim a segurança sobre a propriedade intelectual publicada pode ser considerada boa e reservada ao criador.

**Staking**

Além disso no sistema de Staking dos Token Audius e com base na quantidade de Tokens que você aplica, você recebe uma recompensa gerada pelas taxas de transação. Esse sistema é um Proof od Stake aonde você deixa seus tokens em um lockup para que você consiga participar do funcionamento da rede, recebendo assim uma recompensa por estar ajudando a rede. Assim Audius não depende de nenhuma empresa para continuar funcionando e sim da comunidade.

Há certos parâmetros de staking para cada nó e são eles:
* Nó de Descoberta:
  * Título mínimo (aposta): 200.000 ÁUDIO
  * Garantia máxima (aposta): 7.000.000 ÁUDIO
* Nó de Conteúdo:
  * Título mínimo (aposta): 200.000 ÁUDIO
  * Garantia máxima (aposta): 10.000.0000 ÁUDIO

Esse sistema de aposta mínima garante uma participação suficiente (monetáriamente) para ter efeitos suficientes caso esse sitema dê errado e o máximo evita que o protocolo se torne muito centralizado, essa diferença nos nós de conteúdo se dá por terem requisitos ligeiramente mais altos, razão pela qual eles são capazes de aceitar mais apostas do que os de descoberta.

<a id="org588e4a4"></a>

# Mecanismo de consenso

O mecanismo de consenso do Audius se dá pelo sistema de Governança criado por eles. Assim sendo:

**Governança**

Governança é o processo pelo qual os detentores de tokens de Audio promulgam mudanças no Audius por meio de propostas na rede, ele permite que a comunidade molde diretamente as iterações futuras da plataforma e é o princípio central que orienta a infraestrutura descentralizada do Audius. O local onde você pode encontrar as informações sobre isso é no painel de protocolo na guia Governance.
[Guia Governance do painel de protocolo](https://dashboard.audius.org/governance)

O sistema que verifica se uma proposta vai ser aceita ou não é bem democrático e tem as seguintes necessidades para aprovação:
* Pelo menos 5% de todos os token Audio apostados devem votar na proposta criada
* Mais de 50% dos votos gerais devem ser a favor da proposta
Esse sistema garante um ótimo nível de decisões democráticas.

No Discord na aba Governança é onde as primeiras iterações e ideias de propostas podem ser enviadas para feedback da comunidade, não é necessário ter um feedback sobre qualeur proposta mas é ideal para a boa governança e aprofundamento ou não de um dado tópico antes de enviar o mesmo ao fórum para discussões formais. É uma forma de ver se os membros da comunidade vão aceitar bem ou não e receber feedbaks de alto nível dos membros.
O poder de proposição está correlacionado diretamente com a quantidade de Audio apostada ou delegada para segurança da rede, assim os principais candidatos para propostas em cadeia são os operadores de nó.

O sistema de Governança está em evolução assim como a rede e tem todas as propostas podem ser encontradas aqui.
[Lista de todas as propostas da rede](https://dashboard.audius.org/#/governance) 

Depois que uma votação é concluída e aprovada, o contrato de governança executa a proposta, no entanto o Audius possui um Multisig comunitário como um veto de último recurso, que funciona para envitar qualquer tipo de curto-circuito da rede. Assim um conjunto de 9 membros podem impedir uma proposta maliciosa, caso o Multisig seja utilizada, 6 dos 9 signatários devem assinar uma transação para anular tal proposta prejudicial a rede. Contudo, essa possibilidade de veto também pode parar de existir se uma dada proposta aprovada determinar isso, graças ao sistema de evolução de governança democrático da plataforma.

<a id="orga632e57"></a>

# Função Hash

O hash é feito pelos nós de descoberta, o Audio é um token ERC-20 e a criptografia nativa da rede Audius. Utiliza os TimeStamps para trackeamento.

<a id="org3e33662"></a>

# Anonimidade

A moeda pode ser anônima se o usuário desejar, para se cadastrar na plataforma basta ter um e-mail e senha cadastrados na mesma, porém a conta pode ter os dados do usuário associados, todas os TimeStamps e transações são perfeitamente trackeáveis.


<a id="orgc7fee82"></a>

# Emissão

O sistema de Proof of Stake é um sistema de mineração da moeda Áudio, que faz a manutenção da rede e garante e segurança da mesma. O acúmulo e apostas das moedas por um dado usuário é a forma que este faz valer seu poder no protocolo. Para transferência de valor no ecossistema Audius, stablecoins terceiros permitem que os micropagamentos ocorram em tempo real, sem ser necessário a supervisão de um terceiro confiável para facilitar a distribuição, contabilização ou cobrança. Stablecoins são indexados 1:1 ao dólar americano, fornecendo uma unidade de conta confiável com os benefícos do contrato inteligente.
Graças ao sistema de governança é possível modificar caso se mostre necessário, o sistema de emissão dado a necessidade e acordo comum entre a maioria dos Stakers de Áudio.
A inclusão de recursos extensíveis como NFT's, concursos e tokens de artista permite que se desempenhe um papel ativo no ecossitema Ethereum e DeFi mais amplo, sem ter que recriar os tokens, ferramentas e primitivos, além de dar a capacidade de utility token para a moeda Áudio e possibilitar infinitos usos da mesma.
Como citado anteriormente mo projeto da Audius há cerca de 406 milhões de moedas Áudio em circulação e com um fornecimento total de cerca de 1 bilhão.

<a id="orgd30bf4f"></a>

# Interoperabilidade

O sitema de interoperablidade dos nós Audius se dá que eles estão continuamente enviando instantâneos do protocolo IPFS (InterPlanetary File System) para a rede Ethereum . O IPFS é onde os artistas armazenam suas músicas na rede. Os instantâneos atuam como um mecanismo de segurança, permitindo que os artistas recuperem seu conteúdo do IPFS no Ethereum se o Audius ficar offline. A extensão personalizada da plataforma para IPFS, AudSP, permite que os artistas armazenem e recuperem suas músicas quase instantaneamente. O IPFS é desenvolvido pela Protocol Labs, a empresa por trás do Filecoin e ambos os protocolos cumprem sua missão de criar uma Internet descentralizada. 
[Explicação sobre Filecoin](https://forkast.news/video-audio/what-is-filecoin-decentralized-cloud-data-storage/)

Vale ressaltar que os artistas e criadores de conteúdo podem receber seus Royalties nas suas próprias criptomoedas, seja SDC, SDT ou qualquer alguma outra. 

<a id="orgbc070d2"></a>

# Casos de uso

Um exemplo de caso de uso é o próprio TikTok que não tinha uma plataforma para vincular os sons utilizados nos vídeos e os usuários precisavam gravar o áudio de músicas a serem utilizadas até mesmo com algum microfone perto de alto falante, isso muda todo o sistema e possibilita a inclusão de mídias musicais na máxima qualidade possível. 
Além desse uso por empresas terceiras há diversos aristas aderindo a plataforma (mesmo que essa esteja em sonstante desenvolvimento e melhora), atraídos pelas diversas qualidades e expectativas de lucros mais abundantes com suas propriedades intelectuais, sendo esse um grande chamariz para quem distribui conteúdo e quer se desvencilhar dessa grande "máfia" musical.

<a id="orgdb7acc4"></a>

# Referências

<https://forkast.news/what-is-audius-could-it-be-the-next-spotify/>

<https://dashboard.audius.org/#/governance>

<https://github.com/AudiusProject/audius-protocol/tree/master/discovery-provider>

<https://docs.audius.org/protocol/overview>

<https://forkast.news/video-audio/what-is-filecoin-decentralized-cloud-data-storage/>

<https://forkast.news/what-is-solana-why-hottest-blockchain/>

<https://blog.audius.co/posts/a-primer-on-audio-staking>

<https://audius.org/token>

<https://audius.org/team>

<https://audius.org/>

<https://twitter.com/AudiusProject>

<https://discord.com/invite/audius>

<https://github.com/AudiusProject/audius-protocol>
