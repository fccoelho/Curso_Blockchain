building a merkle tree
######################

in this exercise you are asked to implement a merkle tree. check 
`here <https://en.bitcoin.it/wiki/Protocol_documentation#Merkle_Trees>`__,
`here <http://chimera.labs.oreilly.com/books/1234000001802/ch07.html#merkle_trees>`__
or `here <https://bitcoin.org/en/developer-guide#transaction-data>`__ 
for references. 

if you have any doubts, let us know in the issue you create 
after choosing this assignment.

requirements
============

naming
    class ``MerkleTree``, methods ``leaves`` (to save the input) and 
    ``make_merkle_tree``.

input
    any iterator (such as list) of arbitrary strings.

output
    the merkle tree, obviously. what is the ideal data structure for it?

order
    the algorithm must be deterministic: the same set of strings should return 
    the same merkle tree. (obs.: this is *not* desirable for the real world, 
    but is useful for debugging).

hash function
    please use SHA2-256 as in bitcoin (no need to hash twice as in bitcoin, 
    though).

bonuses
-------

#. add a method ``join_trees`` that takes a merkle tree and another 
   iterator of strings, and appends these to the merkle tree, as in this 
   `picture <https://www.certificate-transparency.org/_/rsrc/1472780088737/log-proofs-work/ct_hash_2.png>`_.

#. add a ``verify_leaf`` method that takes as input a string and a merkle 
   root, and returns the nodes necessary for the verification of the string 
   as a leaf of the merkle tree. it throws an error if the string is not a 
   leaf or if the merkle root is wrong.

#. add a ``delete_leaf`` method that will delete the given input leaves, and 
   re-calculate the merkle tree without them.