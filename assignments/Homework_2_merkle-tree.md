# Building a merkle tree

In this exercise you are asked to implement a merkle tree. check
[here](https://en.bitcoin.it/wiki/Protocol_documentation#Merkle_Trees),
[here](http://chimera.labs.oreilly.com/books/1234000001802/ch07.html#merkle_trees)
or [here](https://bitcoin.org/en/developer-guide#transaction-data)
for references. 

For a gentle introduction to Merkle trees, read [this](https://www.codeproject.com/Articles/1176140/Understanding-Merkle-Trees-Why-use-them-who-uses-t#HowDoesDataVerification(AuditProof)Work13).

If you have any questions, let us know in the issue you create
after choosing this assignment.

## Requirements


- *Naming*

    class ``MerkleTree``, methods ``leaves`` (to save the input) and 
    ``make_merkle_tree``.

- *Input*

    any iterator (such as list) of arbitrary strings.

- *Output*

    the merkle tree, obviously. what is the ideal data structure for it?

- *Order*

    the algorithm must be deterministic: the same set of strings should return 
    the same merkle tree. (obs.: this is *not* desirable for the real world, 
    but is useful for debugging).

- *Hash function*

    please use SHA2-256 as in bitcoin (no need to hash twice as in bitcoin, 
    though).

### Bonuses


1. Add a method ``join_trees`` that takes a merkle tree and another
   iterator of strings, and appends these to the merkle tree, as in this 
   `picture <https://www.certificate-transparency.org/_/rsrc/1472780088737/log-proofs-work/ct_hash_2.png>`_.

1. Add a ``verify_leaf`` method that takes as input a string and a merkle
   root, and returns the nodes necessary for the verification of the string 
   as a leaf of the merkle tree. it throws an error if the string is not a 
   leaf or if the merkle root is wrong.

1. Add a ``delete_leaf`` method that will delete the given input leaves, and
   re-calculate the merkle tree without them.

1. Implement a Merkle-patricia tree (like the one described in Ethereum's yellow paper)
