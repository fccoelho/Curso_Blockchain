# Introduction to Solidity

In this lecture we will  follow the examples from the Solidity documentation to introduce the Solidity language in depth.

## Setting up your development environment

We will run most of the code in this lecture in the `Remix-IDE`. We will run it independently from mist so in order to install it you need to type

```
npm install -g remix-ide
```

Then you can open it by just running the `remix-ide` command. Do it from within the `contracts/Intro to Solidity` directory. After you start it go to you favorite browser and point it to `localhost:8080`.

Later on we will need a private blockchain to deploy contracts to and for that we will use [Ganache](https://truffleframework.com/docs/ganache/quickstart). Please take a moment to install it as well.

## First contact with the language: a Voting contract

We will start to familiarize ourselves with solidity through the [voting contract](/contracts/Intro-to-Solidity/ballot.sol) from the solidity documentation.

The first line of any contract should be what is called the `pragma` which is a declaration of the version number of the compiler for which the contract was written for

```solidity
pragma solidity ^0.4.22;
```

Notice lines in solidity end with a semi-colon.

Then the second thing is the declaration of the contract itself:

```solidity
pragma solidity ^0.4.22;

/// @title Voting with delegation.
contract Ballot {
    // This declares a new complex type which will
    // be used for variables later.
    // It will represent a single voter.
    struct Voter {
        uint weight; // weight is accumulated by delegation
        bool voted;  // if true, that person already voted
        address delegate; // person delegated to
        uint vote;   // index of the voted proposal
    }
}
```

Here we added a few extra lines here declaring a global variable of type `struct`. A struct is a data structure containing one or more vriables. In this case, the struct defines a voter with 4 attributes. Here we are introduced to three other valid types of solidity: `uint` which stands for unsigned int, i.e. positive integers; `bool` meaning a boolean (true|false) type and `address` which represents a valid Ethereum blockchain address. We also see that comment lines are prepended by `\\`.




