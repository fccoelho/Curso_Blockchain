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
depending on how you installed *node* you may need to run the command above as *root* or with *sudo*. Then you can install the OpenZeppelin library.
First you create the project directory.
```bash
mkdir ICO
cd ICO
truffle init
``` 
Then in order to install the latest version of Openzeppelin library, do:
```bash
npm init -y 
npm install --save-exact openzeppelin-solidity@next
```

`npm init -y` initializes the `package.json` file:

```json
{
  "name": "ICO",
  "version": "1.0.0",
  "description": "",
  "main": "truffle-config.js",
  "directories": {
    "test": "test"
  },
  "dependencies": {
    "openzeppelin-solidity": "^1.12.0"
  },
  "devDependencies": {},
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

This file contains metadata about the package and also declares dependencies of your package. Note that a `node_modules` directory is also create at the root of your project directory. this is where libraries needed by your project will reside. Do not fiddle with the contents of this directory. It will be managed by `npm`.

## Contract development
Once You have setup you environment the next thing to do is to start familiarizing yourself with the truffle framework. The best way to do this is by getting your hands dirty in Solidity development and compilation.

As suggested above we can start from the [ERC20 template](https://github.com/OpenZeppelin/openzeppelin-solidity/blob/master/contracts/token/ERC20/ERC20.sol) from Openzeppelin as our token and with the [crowdsale contract](https://github.com/OpenZeppelin/openzeppelin-solidity/blob/master/contracts/crowdsale/Crowdsale.sol) to run the token sale. Copy those templates to the `contracts` directory of your project. 

For our little tutorial, we have [customized them](https://github.com/fccoelho/ICO-playground/tree/2018_project/FunnyToken/contracts) somewhat.

Once you have done that, you are ready to do your first contract compilation using `Truffle`:
```bash
truffle compile
```
If everything comes out ok you should immediately add some tests to your project's contracts. Tests are important as they define the desired functionality of contracts. And help us to keep our contracts safe and valid as we tweek them with new features.

### Testing you contracts
Since we are starting from the templates took from the Openzeppelin solidity project, we can also benefit from the tests they already wrote for them. If look through their [test collection](https://github.com/OpenZeppelin/openzeppelin-solidity/tree/master/test), we can copy two test scripts to our project's test directory: `ERC20.test.sol` and `crowdsale.test.js`. But we will need to modify them to conform our own slightly customized contracts. The crowsale tests will look like this:
```javascript
const { assertRevert } = require('../node_modules/openzeppelin-solidity/test/helpers/assertRevert');
const { ether } = require('../node_modules/openzeppelin-solidity/test/helpers/ether');
const { ethGetBalance } = require('../node_modules/openzeppelin-solidity/test/helpers/web3');

const BigNumber = web3.BigNumber;

const should = require('chai')
  .use(require('chai-bignumber')(BigNumber))
  .should();

const TokenSale = artifacts.require('TokenSale');
const FunnyToken = artifacts.require('FunnyToken');

contract('TokenSale', function ([_, investor, wallet, purchaser]) {
  const rate = new BigNumber(1);
  const value = 10;//ether(42);
  const tokenSupply = new BigNumber('1e18');
  const expectedTokenAmount = rate.mul(value);
  const ZERO_ADDRESS = '0x0000000000000000000000000000000000000000';

  it('requires a non-null token', async function () {
    await assertRevert(
      TokenSale.new(rate, wallet, ZERO_ADDRESS)
    );
  });

  context('with token', async function () {
    beforeEach(async function () {
      this.token = await FunnyToken.new();
    });

    it('requires a non-zero rate', async function () {
      await assertRevert(
        TokenSale.new(0, wallet, this.token.address)
      );
    });

    it('requires a non-null wallet', async function () {
      await assertRevert(
        TokenSale.new(rate, ZERO_ADDRESS, this.token.address)
      );
    });

    context('once deployed', async function () {
      beforeEach(async function () {
        this.tokensale = await TokenSale.new(rate, wallet, this.token.address);
        await this.token.transfer(this.tokensale.address, tokenSupply);
      });

      describe('accepting payments', function () {
        describe('bare payments', function () {
          it('should accept payments', async function () {
            await this.tokensale.send(value, { from: purchaser, gas: 220000 });
          });

          it('reverts on zero-valued payments', async function () {
            await assertRevert(
              this.tokensale.send(0, { from: purchaser })
            );
          });
        });

        describe('buyTokens', function () {
          it('should accept payments', async function () {
            await this.tokensale.buyTokens(investor, { value: value, from: purchaser, gas:220000 });
          });

          it('reverts on zero-valued payments', async function () {
            await assertRevert(
              this.tokensale.buyTokens(investor, { value: 0, from: purchaser, gas:220000 })
            );
          });

          it('requires a non-null beneficiary', async function () {
            await assertRevert(
              this.tokensale.buyTokens(ZERO_ADDRESS, { value: value, from: purchaser, gas:220000 })
            );
          });
        });
      });

      describe('high-level purchase', function () {
        it('should log purchase', async function () {
          const { logs } = await this.tokensale.sendTransaction({ value: value, from: investor, gas:220000 });
          const event = logs.find(e => e.event === 'TokensPurchased');
          should.exist(event);
          event.args.purchaser.should.equal(investor);
          event.args.beneficiary.should.equal(investor);
          event.args.value.should.be.bignumber.equal(value);
          event.args.amount.should.be.bignumber.equal(expectedTokenAmount);
        });

        it('should assign tokens to sender', async function () {
          await this.tokensale.sendTransaction({ value: value, from: investor, gas:220000 });
          (await this.token.balanceOf(investor)).should.be.bignumber.equal(expectedTokenAmount);
        });

        it('should forward funds to wallet', async function () {
          const pre = await ethGetBalance(wallet);
          await this.tokensale.sendTransaction({ value, from: investor, gas: 220000 });
          const post = await ethGetBalance(wallet);
          post.minus(pre).should.be.bignumber.equal(value);
        });
      });

      describe('low-level purchase', function () {
        it('should log purchase', async function () {
          const { logs } = await this.tokensale.buyTokens(investor, { value: value, from: purchaser, gas:220000 });
          const event = logs.find(e => e.event === 'TokensPurchased');
          should.exist(event);
          event.args.purchaser.should.equal(purchaser);
          event.args.beneficiary.should.equal(investor);
          event.args.value.should.be.bignumber.equal(value);
          event.args.amount.should.be.bignumber.equal(expectedTokenAmount);
        });

        it('should assign tokens to beneficiary', async function () {
          await this.tokensale.buyTokens(investor, { value, from: purchaser, gas:220000 });
          (await this.token.balanceOf(investor)).should.be.bignumber.equal(expectedTokenAmount);
        });

        it('should forward funds to wallet', async function () {
          const pre = await ethGetBalance(wallet);
          await this.tokensale.buyTokens(investor, { value, from: purchaser , gas:220000});
          const post = await ethGetBalance(wallet);
          post.minus(pre).should.be.bignumber.equal(value);
        });
      });
    });
  });
});
```
