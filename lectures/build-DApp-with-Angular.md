# Building a DApp with Angular
In this lecture we will start developing the frontend for our [ICO](build-your-own-ICO.md).
We will use [Angular](https://angular.io) as the framework for this web application.

## Getting started
We are going to use the latest version of Angular, which requires a reasonably modern version of Node. So start by updating your version of Node:
```bash
$ sudo npm cache clean -f
$ sudo npm install -g n
$ sudo n latest
```
Then you can install Angular:
```bash
$ sudo npm install -g @angular/cli
```
Now that you have Angular you are ready to create your app.
```bash
$ ng new frontend-js
```
After a few seconds you should have a functional minimal application which you can run with:
```bash
$ cd frontend-js
$ ng serve
```
and point you browser to [ http://localhost:4200/](http://localhost:4200/).

## Installing blockchain specific libraries
Since we are developing a frontend to solidity code running on a blockchain, we will need some libraries to help us interact with the ethereum blockchain. From within your Angular app directory, run:
```bash
$ npm install web3
$ npm install truffle-contract
``` 
`truffle-contract` provides contract abstraction. The contract abstractions are wrapper code that makes interaction with your contract easier.
```bash
$ ng generate service ethcontract
CREATE src/app/ethcontract.service.spec.ts (404 bytes)
CREATE src/app/ethcontract.service.ts (140 bytes)

```
