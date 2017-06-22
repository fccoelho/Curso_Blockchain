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

## Iniciando uma rede privada

```bash
$ geth --ipcpath <test-chain-directory>/geth.ipc --datadir <test-chain-directory> --dev console

```
Notem o comando console no final. Ele significa que após iniciar nossa 
blockchain privada, o Geth vai abrir um console para podermos interagir 
com a blockchain.

Agora que iniciamos uma rede privada, podemos iniciar o Mist apontando 
para esta mesma rede. 

## Iniciando o Mist

```bash
$ mist --rpc <test-chain-directory>/geth.ipc
```
