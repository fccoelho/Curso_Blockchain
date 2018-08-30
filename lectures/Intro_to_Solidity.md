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

For this contract's constructor, one argument is required which is a list of proposal names. `proposalNames` is a array of `bytes32` strings. The variable `msg.sender` is the address of the user that deployed the contract.

### The remaining logic

```solidity
    // Give `voter` the right to vote on this ballot.
    // May only be called by `chairperson`.
    function giveRightToVote(address voter) public {
        // If the first argument of `require` evaluates
        // to `false`, execution terminates and all
        // changes to the state and to Ether balances
        // are reverted.
        // This used to consume all gas in old EVM versions, but
        // not anymore.
        // It is often a good idea to use `require` to check if
        // functions are called correctly.
        // As a second argument, you can also provide an
        // explanation about what went wrong.
        require(
            msg.sender == chairperson,
            "Only chairperson can give right to vote."
        );
        require(
            !voters[voter].voted,
            "The voter already voted."
        );
        require(voters[voter].weight == 0);
        voters[voter].weight = 1;
    }

    /// Delegate your vote to the voter `to`.
    function delegate(address to) public {
        // assigns reference
        Voter storage sender = voters[msg.sender];
        require(!sender.voted, "You already voted.");

        require(to != msg.sender, "Self-delegation is disallowed.");

        // Forward the delegation as long as
        // `to` also delegated.
        // In general, such loops are very dangerous,
        // because if they run too long, they might
        // need more gas than is available in a block.
        // In this case, the delegation will not be executed,
        // but in other situations, such loops might
        // cause a contract to get "stuck" completely.
        while (voters[to].delegate != address(0)) {
            to = voters[to].delegate;

            // We found a loop in the delegation, not allowed.
            require(to != msg.sender, "Found loop in delegation.");
        }

        // Since `sender` is a reference, this
        // modifies `voters[msg.sender].voted`
        sender.voted = true;
        sender.delegate = to;
        Voter storage delegate_ = voters[to];
        if (delegate_.voted) {
            // If the delegate already voted,
            // directly add to the number of votes
            proposals[delegate_.vote].voteCount += sender.weight;
        } else {
            // If the delegate did not vote yet,
            // add to her weight.
            delegate_.weight += sender.weight;
        }
    }

    /// Give your vote (including votes delegated to you)
    /// to proposal `proposals[proposal].name`.
    function vote(uint proposal) public {
        Voter storage sender = voters[msg.sender];
        require(!sender.voted, "Already voted.");
        sender.voted = true;
        sender.vote = proposal;

        // If `proposal` is out of the range of the array,
        // this will throw automatically and revert all
        // changes.
        proposals[proposal].voteCount += sender.weight;
    }

    /// @dev Computes the winning proposal taking all
    /// previous votes into account.
    function winningProposal() public view
            returns (uint winningProposal_)
    {
        uint winningVoteCount = 0;
        for (uint p = 0; p < proposals.length; p++) {
            if (proposals[p].voteCount > winningVoteCount) {
                winningVoteCount = proposals[p].voteCount;
                winningProposal_ = p;
            }
        }
    }

    // Calls winningProposal() function to get the index
    // of the winner contained in the proposals array and then
    // returns the name of the winner
    function winnerName() public view
            returns (bytes32 winnerName_)
    {
        winnerName_ = proposals[winningProposal()].name;
    }
}
```
The rest of the code does not contain many surprises or new language elements. The `while` loop in the `delegate` function is something to worry about because it can lead to vry large gas costs. We should try to avoid at all costs, loops without clear ending conditions.

## Other example contracts
In the [/contracts/Intro-to-Solidity](/contracts/Intro-to-Solidity) directory you can find other contracts (from the Solidity official docs) to study. I suggest you open them in the remix IDE compile and deploy then on a private blockchain to fully understand how they work.

In the [Open Auction contract](/contracts/Intro-to-Solidity/openauction.sol), the concept of a payable contract is introduced along with new language elements such as `events`.

In the [Blind Auction contract](/contracts/Intro-to-Solidity/blindauction.sol), we introduce `modifiers`, `requires` and the use of absolute time in a contract. We also use the builtin `keccak256`cryptographic hash function to make the auction blind.

In the [Purchase contract](/contracts/Intro-to-Solidity/purchase.sol), a very common application, a safe remote purchase based exclusively on a smart-contract is introduced, using the elements of the language already introduced in previous contracts.

Finally, a complete implementation of a micropayment channel is presented, complete with both the smart-contract and bits of javascript code to interact with the channel. Here we refer the reader to the official docs as the example includes multiple files.
