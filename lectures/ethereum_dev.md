# Preparando-se para desenvolver em Ethereum

Neste documento vamos aprender a como configurar um ambente de 
desenvolvimento para *Smart Contracts*.

Para isso é necessário instalar tanto o cliente Geth quando a IDE Remix.
Ambos estão disponíveis na site oficial do Ethereum.

O Geth é o cliente oficial do Ethereum, e o Remix é parte do frontend 
Mist, que serve de carteira, e também para desenvolvimento e deploy de 
contratos.

Antes de começar a desenvolver, precisamos iniciar Geth em uma rede 
privada.

No Ubuntu estes componentes podem ser instalados através dos seguintes comandos:

```
sudo apt-get install software-properties-common
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install ethereum
```

Caso voce prefira rodar um cliente ethereum a partir de uma imagem docker, siga [este tutorial](https://github.com/ethereum/go-ethereum/wiki/Running-in-Docker). Se for instalar no MacOS, use [este tutorial](https://github.com/ethereum/go-ethereum/wiki/Installation-Instructions-for-Mac)

## Iniciando uma rede privada

O promeiro passo no estabelecimento de uma rede privada é a criação de um bloco "Genesis".

Para isso precisamos criar, no diretório de dados da nossa rede privada um arquivo json com o seguinte conteudo:
```JSON
{
    "config": {
        "chainId": 15,
        "homesteadBlock": 0,
        "eip155Block": 0,
        "eip158Block": 0
    },
    "difficulty": "20000",
    "gasLimit": "2100000",
    "alloc": {
        "7df9a875a174b3bc565e6424a0050ebc1b2d1d82": { "balance": "300000" },
        "f41c74c9ae680c1aa78f42e5647a62f353b7bdde": { "balance": "400000" }
    }
}
```

Podemos chamá-lo de "meuGenesis.json".
Todos os pares que irão executar o `geth` devem possuir o mesmo bloco "Genesis".

Agora precisamos inicializar nossa blockchain com este bloco.

```bash
geth --datadir="eth-test-chain" init meuGenesis.json
```

Agora podemos iniciar o nosso nó com o seguinte comando

```bash
geth --ipcpath eth-test-chain/geth.ipc --datadir eth-test-chain --networkid 15
```

Agora precisamos iniciar um nó de bootstrap no qual os pares possam se conectar e

```bash
bootnode --genkey=boot.key
bootnode --nodekey=boot.key
```

Este comando vai retornar uma url para o seu enode que outros nós podem usar para se conectar
à sua rede privada. Substitua `[::]` pelo seu IP acessível aos outros nós.

Para conectar outros nós ao nó de boot, basta iniciar  geth nas outras máquinas passando a url
no enode obitda acima:

```bash
geth --datadir eth-test-chain --networkid 15 --bootnodes <bootnode-enode-url>
```

Podemos ainda abrir um console interativo:

```bash
geth --datadir eth-test-chain --networkid 15 --rpc --rpcapi="db,eth,net,web3,personal" --dev console
```

Notem o comando console no final. Ele significa que após iniciar nossa
blockchain privada, o `geth` vai abrir um console para podermos interagir 
com a blockchain.

Agora que iniciamos uma rede privada, podemos iniciar o Mist apontando 
para esta mesma rede. 

## Iniciando o Mist

O Mist precisa ser instalado separadamente do resto da stack do ethereum. Para isso consulte as [releases](https://github.com/ethereum/mist/releases) do Mist e baixe a que estiver de acordo com a versao do ethereum que voce tem instalada.

```bash
mist --rpc eth-test-chain/geth.ipc
```

Uma vez aberto o Mist, crie uma carteira. Este passo é muito importante pois para publicarmos um contrato precisaremos de Ether.

## Minerando Ether na cadeia privada.

Minerar Ether na rede principal do Ethereum é uma tarefa computacionalmente ingrata sem um hardware extremamente poderoso. Mas na nossa cadeia privada é facílimo! Então vamos minerar algumas moedas para financiar o nosso desenvolvimento. 

No console do geth, que abrimos acima, basta dar o seguinte comando:

```
> miner.start
```

Olhe agora na sua carteira no Mist o dinheiro se acumular! quando achar que já tem suficiente, basta dar o seguinte comando:

```
> miner.stop()
```

Não se preocupe que você sempre pode minerar mais quando precisar.

## Verificando o Saldo

Você pode descobrir através do console qual a conta default:

```
> eth.coinbase
"0x12471750cebdb1af31394910e00ce737d4818948"
```

e também o seu saldo:

```
> eth.getBalance(eth.coinbase)
160000000000000000000
```

## Enviando transações

Agora que temos alguns *ether*, podemos enviar algum dinheiro para uma segunda conta. Primeiro crie uma segunda carteira no Mist. Depois, no console, liste as carteiras:

```
> eth.accounts
["0x12471750cebdb1af31394910e00ce737d4818948", "0x8777709d62b83272452621411802e311637ed723"]
```

Vamos agora enviar algum dinheiro, mas antes precisamos "destrancar" nossa conta:

```
> personal.unlockAccount(eth.coinbase)
Unlock account 0x12471750cebdb1af31394910e00ce737d4818948
Passphrase: 
true
```

Agora sim podemos enviar dinheiro a partir dela:

```
> eth.sendTransaction({from: eth.accounts[0], to: eth.accounts[1], value: 10})
INFO [07-15|11:45:21] Submitted transaction                    fullhash=0xed0c58101b936986dee06af5a54485ba0b43a81e18909e97d5ac985984a8cdbd recipient=0x8777709d62b83272452621411802e311637ed723
"0xed0c58101b936986dee06af5a54485ba0b43a81e18909e97d5ac985984a8cdbd"
```

Se olharmos o saldo na nossa segunda carteira através do Mist, veremos que continua vazia. O que aconteceu? vamos consultar o status da nossa transação no console:

```
> eth.pendingTransactions
[{
    blockHash: null,
    blockNumber: null,
    from: "0x12471750cebdb1af31394910e00ce737d4818948",
    gas: 90000,
    gasPrice: 0,
    hash: "0xed0c58101b936986dee06af5a54485ba0b43a81e18909e97d5ac985984a8cdbd",
    input: "0x",
    nonce: 0,
    r: "0x75d4c5615df9effdb114857e82057b750f422a31610e05fd6fa5a48b8d89b879",
    s: "0x464de5301b694334cf4f55c0a45dec5790ee43cf25a55ab7237a98d669fcfd62",
    to: "0x8777709d62b83272452621411802e311637ed723",
    transactionIndex: 0,
    v: "0xa95",
    value: 10
}]
```

Vemos que nossa transação está pendente, não foi executada. Claro! para concluir qualquer transação, a cadeia tem que ser minerada para inserção da transação! Basta ligar novamente a mineração para vermos a transação se completar.

Mas a transação que fizemos foi em unidades *Wei* e não *ether* para corrigir isso e envia *ether*, temos que fazer outra transação:

```
> eth.sendTransaction({from: eth.accounts[0], to: eth.accounts[1], value: web3.toWei(10, "ether")})
```



