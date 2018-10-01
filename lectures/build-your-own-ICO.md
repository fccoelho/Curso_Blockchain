# Build your own ICO

ICOs (Initial Coin Offerings) are (still) a dominating phenomenon in the smart-contract world.
 A full ICO is much more than software development, depending for its success on a soud business model behind it and lots of marketing.
 
 An ICO is basically a *crowdsale* of special-purpose tokens usually conducted to raise capital for a business.  There are other reasons to create a tokes, of course but most ICOs aim at raising funds. In any case, no matter the purpose of your token If it does not get sold, it remains useless. So the content of this lecture is relevant for a wide variety of ICOs.
 
 ## The contracts
An ICO needs at least two contracts: *the token contract* and a *crowdsale* contract to sell the tokens.
For this exercise we will use a basic ERC20 contract whichwe have already studied on a [previous lecture](token-contracts.md).

We will also develop a crowdsale contract and for that we will start from the template [made available](https://github.com/OpenZeppelin/openzeppelin-solidity/blob/master/contracts/crowdsale/Crowdsale.sol) from the OpenZeppelin project. 

## Setting up the project
For this project we will use the Truffle framework. We will work step-by-step here in this setup, however if you wish to learn more please check out [this video](https://www.youtube.com/watch?v=Zwc98_AvQ2Y).

First let's install the basic software. I'll assume that if you are following this course you will already have installed nodejs and Ganache on your computer. If you have not, please follow the instructions on [this lecture](Solidity%20development%20environment.md).

the following command will install Truffle:
```bash
npm install -g truffle
```
denpending on how you installed *node* you may need to run the command above as *root* or with *sudo*. Then you can install the OpenZeppelin library.
```bash
npm install -g openzeppelin-solidity
```

