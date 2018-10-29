# Building a DApp with Webpack
In this lecture we will start developing the frontend for our [ICO](build-your-own-ICO.md).
We will base the javascript frontend on the [Webpack box](https://github.com/truffle-box/webpack-box) provided by truffle. However, to make it work with our contracts we will modify the truffle box a little.

## Getting started
We are going to use the latest version of Webpack, which requires a reasonably modern version of Node. So start by updating your version of Node:
```bash
$ sudo npm cache clean -f
$ sudo npm install -g n
$ sudo n latest
```
Let's start by creating our own frontend project folder
```bash
$ mkdir jf-frontend
$ cd js-frontend
```
Now let's unbox the webpack example.
```bash
$ truffle unbox webpack
```
After a few seconds you should have the basic code. Now let's get rid of its original contracts and customize the code to run with our FunnyToken ICO contracts:
```bash
$ rm -rf contracts
$ rm -rf migrations
$ rm truffle.js 
$ rm test
```
Now we are left with just the frontend code. We will now edit the app code. Let's start by `app/scripts/index.js`
it should be edited to become like below:
```javascript
// Import the page's CSS. Webpack will know what to do with it.
import '../styles/app.css'

// Import libraries we need.
import {default as Web3} from 'web3'
import {default as contract} from 'truffle-contract'

// Import our contract artifacts and turn them into usable abstractions.
import funnyTokenArtifact from '../../../FunnyToken/build/contracts/FunnyToken.json'
import tokenSaleArtifact from '../../../FunnyToken/build/contracts/TokenSale'

// FunnyToken is our usable abstraction, which we'll use through the code below.
const FunnyToken = contract(funnyTokenArtifact)
const TokenSale = contract(tokenSaleArtifact)

// The following code is simple to show off interacting with your contracts.
// As your needs grow you will likely need to change its form and structure.
// For application bootstrapping, check out window.addEventListener below.
let accounts
let account

const App = {
    start: function () {
        const self = this

        // Bootstrap the FunnyToken abstraction for Use.
        FunnyToken.setProvider(web3.currentProvider)

        // Get the initial account balance so it can be displayed.
        web3.eth.getAccounts(function (err, accs) {
            if (err != null) {
                alert('There was an error fetching your accounts.')
                return
            }

            if (accs.length === 0) {
                alert("Couldn't get any accounts! Make sure your Ethereum client is configured correctly.")
                return
            }

            accounts = accs
            account = accounts[0]

            self.refreshBalance()
        })
    },

    setStatus: function (message) {
        const status = document.getElementById('status')
        status.innerHTML = message
    },

    refreshBalance: function () {
        const self = this

        let funny
        FunnyToken.deployed().then(function (instance) {
            funny = instance
            return funny.balanceOf.call(account, {from: account})
        }).then(function (value) {
            const balanceElement = document.getElementById('balance')
            balanceElement.innerHTML = value.valueOf()
        }).catch(function (e) {
            console.log(e)
            self.setStatus('Error getting balance; see log.')
        })
    },

    sendCoin: function () {
        const self = this

        const amount = parseInt(document.getElementById('amount').value)
        const receiver = document.getElementById('receiver').value

        this.setStatus('Initiating transaction... (please wait)')

        let funny
        FunnyToken.deployed().then(function (instance) {
            funny = instance
            return funny.sendCoin(receiver, amount, {from: account})
        }).then(function () {
            self.setStatus('Transaction complete!')
            self.refreshBalance()
        }).catch(function (e) {
            console.log(e)
            self.setStatus('Error sending coin; see log.')
        })
    }
}

window.App = App

window.addEventListener('load', function () {
    // Checking if Web3 has been injected by the browser (Mist/MetaMask)
    if (typeof web3 !== 'undefined') {
        console.warn(
            'Using web3 detected from external source.' +
            ' If you find that your accounts don\'t appear or you have 0 FunnyToken,' +
            ' ensure you\'ve configured that source properly.' +
            ' If using MetaMask, see the following link.' +
            ' Feel free to delete this warning. :)' +
            ' http://truffleframework.com/tutorials/truffle-and-metamask'
        )
        // Use Mist/MetaMask's provider
        window.web3 = new Web3(web3.currentProvider)
    } else {
        console.warn(
            'No web3 detected. Falling back to http://127.0.0.1:8545.' +
            ' You should remove this fallback when you deploy live, as it\'s inherently insecure.' +
            ' Consider switching to Metamask for development.' +
            ' More info here: http://truffleframework.com/tutorials/truffle-and-metamask'
        )
        // fallback - use your fallback strategy (local node / hosted node + in-dapp id mgmt / fail)
        window.web3 = new Web3(new Web3.providers.HttpProvider('http://127.0.0.1:8545'))
    }

    App.start()
})
```
We are still going to modify this file as we improve our DApp frontend. But for now, just code should do.
You will also need to modify `app/index.html` to look like this:
```html
<!DOCTYPE html>
<html>
<head>
  <title>FunnyToken - Join our Fun ICO!</title>
  <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,700' rel='stylesheet' type='text/css'>
  <script src="./app.js"></script>
</head>
<body>
  <h1>FunnyToken</h1>
  <h2>The Funniest ICO Ever!</h2>
  <h3>You have <span class="black"><span id="balance"></span> Funny</span></h3>

  <br>
  <h1>Buy FunnyToken!</h1>
  <p>Send Ether to this Address:</p>
  <br><label for="amount">Amount:</label><input type="text" id="amount" placeholder="e.g., 95"></input>
  <br><label for="receiver">Your Address:</label><input type="text" id="receiver" placeholder="e.g., 0x93e66d9baea28c17d9fc393b53e3fbdd76899dae"></input>
  <br><br><button id="send" onclick="App.sendCoin()">Send FunnyToken</button>
  <br><br>
  <span id="status"></span>
  <br>
  <span class="hint"><strong>Hint:</strong> open the browser developer console to view any errors and warnings.</span>
</body>
</html>

```



Let's now compile and migrate the contracts of Our ICO. Make sure you have started either Ganache or `ganache-cli` and from inside the FunnyToken directory run:
```bash
$ truffle compile
$ truffle migrate
``` 
This should deploy the FunnyToken Contract.



## Running the frontend App
Now we can run our frontend code. From the `js-frontend` directory, run:
```bash
$ npm run dev
``` 
If everything goes well, point your browser to [localhost:8080](http://localhost:8080) to see your app. 

