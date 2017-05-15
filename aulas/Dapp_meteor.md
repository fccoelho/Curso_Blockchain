 
# Criando um Frontend para o seu contrato

Depois de publicado o nosso contrato é apenas um programa na blockchain com uma  
API, para facilitar a interação do publico-alvo com o contrato.

Para este fim vamos construir um web app muito simples usando a framework
[meteor](www.meteor.com) que é voltada para a construção de aplicativos em uma 
página de código que podem ser deployed tanto na web quanto em ambientes mobile.

## Instalando o Meteor

para instalar o Meteor, basta executar o seguinte comando:

```bash
$ curl https://install.meteor.com/ | sh
```

## Criando o app

Vamos seguir nosso tutorial e criar o applicativo para nosso contrato de lista 
de Presença.

```bash
$ meteor create presencaDapp
$ cd presencaDapp
```

em seguida vamos adicionar um pacote o nosso projeto: o web3 do Ethereum

```bash
$ meteor add ethereum:web3
$ meteor add ethereum:dapp-styles
$ meteor add ethereum:tools
```

### Configurando o Dapp

Crie um diretorio lib  e dentro dele um arquivo chamado `init.js`.

```bash
$ mkdir lib
$ touch lib/init.js
```

dentro deste arquivo coloque o seguinte código:

```javascript
if(typeof web3 === 'undefined')
    web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'));
```

Agora podemos já executar nosso aplicativo pela primeira vez, mas antes temos 
que iniciar o geth na nossa chain privada:

```bash
$ geth --ipcpath Downloads/dev_eth_chain/geth.ipc --datadir 
Downloads/dev_eth_chain/ --rpc --rpccorsdomain "http://localhost:3000" --dev 
console
```

e iniciar o aplicativo:

```bash
$ meteor
```

Agora é só abrir o browser em localhost:3000.
