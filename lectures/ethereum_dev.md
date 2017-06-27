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
    "difficulty": "200000000",
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

```
geth --datadir="eth-test-chain" init meuGenesis.json
```

Agora podemos iniciar o nosso nó com o seguinte comando

```bash
geth --ipcpath eth-test-chain/geth.ipc --datadir eth-test-chain --networkid 15
```

Agora precisamos iniciar um nó de bootstrap no qual os pares possam se conectar e

```
bootnode --genkey=boot.key
bootnode --nodekey=boot.key
```

Este comando vai retornar uma url para o seu enode que outros nós podem usar para se conectar
à sua rede privada. Substitua `[::]` pelo seu IP acessível aos outros nós.

Para conectar outros nós ao nó de boot, basta iniciar  geth nas outras máquinas passando a url
no enode obitda acima:

```
geth --datadir eth-test-chain --networkid 15 --bootnodes <bootnode-enode-url>
```

Agora só falta configurar um processo minerador para esta blockchain, usando como etherbase um dos endereços definidos no bloco genesis.
Este endereço vai receber

```
geth --datadir eth-test-chain --networkid 15 --mine --minerthreads=1 --etherbase="7df9a875a174b3bc565e6424a0050ebc1b2d1d82"
```

Podemos ainda abrir um console interativo:

```
geth --datadir eth-test-chain --networkid 15 --dev console
```

Notem o comando console no final. Ele significa que após iniciar nossa
blockchain privada, o Geth vai abrir um console para podermos interagir 
com a blockchain.

Agora que iniciamos uma rede privada, podemos iniciar o Mist apontando 
para esta mesma rede. 

## Iniciando o Mist

```bash
mist --rpc <eth-test-chain>/geth.ipc
```
