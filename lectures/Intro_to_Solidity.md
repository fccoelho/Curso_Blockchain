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

### Public and internal variables

Like on other languages, in Solidity you can set the visibility of variables and functions of your contract.

```solidity
    // This is a type for a single proposal.
    struct Proposal {
        bytes32 name;   // short name (up to 32 bytes)
        uint voteCount; // number of accumulated votes
    }

    address public chairperson;

    // This declares a state variable that
    // stores a `Voter` struct for each possible address.
    mapping(address => Voter) public voters;

    // A dynamically-sized array of `Proposal` structs.
    Proposal[] public proposals;
``` 
In the code above, we declare a few other variables which have their visibility specified. This code follow imediately the previous codeblock within the contract block: `contract Ballot{...}`.

Structs can be seen as new "types" as they just define a structure. Later variables will be defined based on these new "types". Above, the variables `chairperson`, `voters` and `proposals` are public variables meaning their values will be visible on the blockchain to anyone which goes to the contract address. Other basic types are introduced here: `bytes32` which is used to store strings of up to 32 bytes in size; `mapping` which is a set of variable size of keys mapped to values. Both types (of keys and values) must be declared when the map is created, so they cannot, as in a Python dictionary, use any mix of types for keys and values. In this cases the voters mapping maps addresses to Voter (declared previously). We also meet another new "type" which is the array which constitutes a collection of a single type, also here of an variable size. Here the proposals array collects Proposals, which have been defined above.


### Initializing the contract
Every contract can contain code which executed only at the moment the contract is created. This code resides on a special block of code called a constructor. Only one constructor is allowed per contract.

```solidity
/// Create a new ballot to choose one of `proposalNames`.
    constructor(bytes32[] memory proposalNames) public {
        chairperson = msg.sender;
        voters[chairperson].weight = 1;

        // For each of the provided proposal names,
        // create a new proposal object and add it
        // to the end of the array.
        for (uint i = 0; i < proposalNames.length; i++) {
            // `Proposal({...})` creates a temporary
            // Proposal object and `proposals.push(...)`
            // appends it to the end of `proposals`.
            proposals.push(Proposal({
                name: proposalNames[i],
                voteCount: 0
            }));
        }
    }
```

For this contract's constructor,


